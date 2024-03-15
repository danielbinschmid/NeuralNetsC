#*****************************************************************

CC = gcc
RM = rm

ROOT=../
LIB=${ROOT}/lib

CFLAGS=-I${LIB}/sml -g
LFLAGS=-L${LIB}/sml ${LIB}/sml/sml.lib

#*****************************************************************

all: linear
.PHONY: all

linear    : linear.c
	$(CC) $(CFLAGS) -o $@  linear.c  $(LFLAGS) -lm

.PHONY: clean
clean:
	$(RM) -f *.o linear
	$(RM) -rf *.dSYM
