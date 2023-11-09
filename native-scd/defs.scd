var srvProg = Platform.resourceDir.quote;
Server.program = "start /B /HIGH /D % scsynth.exe".format(srvProg);

s.waitForBoot{
  w = Synth("simpleWobble");
}

