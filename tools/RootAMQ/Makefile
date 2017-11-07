# Makefile template for shared library

CC = g++ # C++ compiler
CFLAGS = -c -fPIC -Wall -Wextra -O2 -g # C flags
LDFLAGS = -shared  # linking flags

TARGET_LIB = libRootMQ.so # target lib

SRCS = RootMQ.cpp # source files
OBJS = RootMQ.o
HEADERS =  RootMQ.h
USR_INCLUDES += -I./  -I/usr/include/apr-1 -I/usr/include/activemq-cpp-3.9.3

.PHONY: all
all: ${TARGET_LIB}

$(TARGET_LIB): $(OBJS)
	$(CC) ${LDFLAGS} -o $@ $^

$(OBJS): ${SRCS} ${HEADERS}
	$(CC) $(CFLAGS) ${USR_INCLUDES} -o ${OBJS} ${SRCS}


.PHONY: clean
clean:
	-${RM} ${TARGET_LIB} ${OBJS}

