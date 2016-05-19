
/* header file for v288.c */

/* LOW-level functions */

void v288ActiveLoop(int spas);
int v288Transmit(UINT32 addr, UINT32 offset, UINT16 vmedat, int spas);
int v288Wait(UINT32 addr, int spas);
int v288Reset(UINT32 addr);


/* MID-level functions */

int v288Send1(UINT32 addr, UINT16 crate, UINT16 code, int delay);
int v288Send2(UINT32 addr, UINT16 value, int delay);
int v288Send3(UINT32 addr, int delay);
int v288Send(UINT32 addr, UINT16 crate, UINT16 code, UINT16 *value);
int v288Get(UINT32 addr, int nw, UINT16 *buffer);


/* CAEN1527-style API functions */

int  CAENHVInitSystem(const char *SystemName, int LinkType, void *Arg,
                      const char *UserName, const char *Passwd);

int  CAENHVDeinitSystem(const char *SystemName);

char *CAENHVGetError(const char *SystemName);

int  CAENHVGetCrateMap(const char *SystemName, ushort *NrOfSlot,
                      ushort **NrofChList, char **ModelList,
                      char **DescriptionList, ushort **SerNumList,
                      unsigned char **FmwRelMinList, 
                      unsigned char **FmwRelMaxList);

int  CAENHVGetChParam(const char *SystemName, ushort slot, const char *ParName,
                      ushort ChNum, const ushort *ChList, void *ParValList);

int  CAENHVSetChParam(const char *SystemName, ushort slot, const char *ParName,
                      ushort ChNum, const ushort *ChList, void *ParValue);

int  CAENHVGetChParamProp(const char *SystemName, ushort slot, ushort Ch,
                      const char *ParName, const char *PropName, void *retval);

///=================== my: ========================================
//unsigned char vmeRead8(volatile unsigned char *addr);
//void vmeWrite8(volatile unsigned char *addr, unsigned char val);
unsigned short vmeRead16(volatile unsigned short *addr);
void vmeWrite16(volatile unsigned short *addr, unsigned short val);
//unsigned int vmeRead32(volatile unsigned int *addr);
//void vmeWrite32(volatile unsigned int *addr, unsigned int val);
///================================================================

