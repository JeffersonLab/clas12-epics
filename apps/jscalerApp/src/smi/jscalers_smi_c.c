
#ifdef USE_SMI
#include "smiuirtl.h"
#endif

#include "common.h"

int
ccompiled_callto_smiui_send_command(char * name, char * command)
{
#ifdef USE_SMI
  smiui_send_command(name, command);
#endif
  return 0;
}
