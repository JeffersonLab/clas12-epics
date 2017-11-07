class RootMQ {
  
 private:
  RootMQ( const RootMQ& );
  bool isConnected;
  
 public:
  RootMQ(const char *broker_host);
  bool GetConnectionStatus(){return isConnected;};
  int SendMessage(const char *topic, char *msg);
  void jStart (char *jstring);
  void jEnd (char *jstring);
  void jAddInt(char *jstring, const char *name, int data, const char *format="%d");
  void jAddDouble(char *jstring,  const char *name, double data, const char *format="%le");
  void jAddString(char *jstring,  const char *name, char *data);
  void jAddIntArray(char *jstring,  const char *name, int *data, int len, const char *format="%d");
  void jAddDoubleArray(char *jstring,  const char *name, double *data, int len, const char *format="%le");
  void jAddStringArray(char *jstring,  const char *name, char **data, int len);
  
  virtual ~RootMQ(){};
};

