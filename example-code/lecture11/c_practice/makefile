SOURCE := $(wildcard *.c)
OBJS := $(patsubst %.c,%.o, $(SOURCE))

TARGET := main
CC := gcc
LIBS :=


all: $(TARGET)

objs: $(OBJS)

clean: 
	rm -rf *.so
	rm -rf *.o
	rm -rf $(TARGET)

$(TARGET): $(OBJS)
	$(CC) -o $@ $(OBJS)