#include <stddef.h>
const size_t output_len = 10;
uint8_t output[] __attribute__((section("output_data_sec"), aligned(16))) = "\x00\x00\x00\x00\xf6\x3f\x95\x3c\xf0\x66\x28\x3e\x00\x00\x00\x00\x14\xdf\x79\x3d\x00\x00\x00\x00\xa4\x25\x2c\x3e\x00\x00\x00\x00\x2a\x51\xa0\x3c\x15\xd8\x1c\x3e";

