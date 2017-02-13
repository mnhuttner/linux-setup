#!/usr/bin/perl
$|++;
use strict;
myInit();
getRepos();
1;
sub myInit {
  $ENV{GIT_SSH_COMMAND} = "/usr/bin/ssh -o StrictHostKeyChecking=no"; # -i $ENV{HOME}/.ssh/id_rsa";
  myExec("pkill ssh-agent");
  open my $fh, "ssh-agent -s 2>&1 |" or die "Could not exec ssh-agent: $!\n";
  while (<$fh>) {
    s/;//g;
    if (m/^\s*(\S+?)\s*=\s*(\S+)/) { $ENV{$1} = "$2"; }
  } close $fh;
  system("env|grep SSH");
  myExec("ssh-add ~/.ssh/id_rsa </dev/null &>/dev/null");
  #myExec("ssh -vT git\@github.com");
}
sub myExec {
  my $cmd = shift;
  print "# $cmd\n";
  system($cmd) == 0 or warn "Error: $!\n";
}
sub getRepos {
  my $name = "mnhuttner";
  my $cmd = "curl -s https://api.github.com/users/$name/repos";
  print "$cmd\n";
  open my $fh, "$cmd 2>&1 |" or die "Could not exec $cmd: $!\n";
  while (<$fh>) {
    chomp;
    s/"//g; s/,//g;
    if (m/\sname:\s*(\S+)/) {
      my $repo = $1;
      if (-d $repo) {
	print "# $repo exists, skipping\n"; next;
      }
      my $git = "git clone git\@github.com:/$name/$repo $repo";
      myExec($git);
    }
  } close $fh;
}
