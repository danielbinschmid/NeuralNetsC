#include "tvmgen_default.h"

// input and output data header
#include "input.h"
#include "output.h"
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char** argv) {
    printf("Starting simulation.\n");

    struct tvmgen_default_inputs inputs = {
        .in = input,
    };

    void* output_buffer = malloc(163840 * sizeof(float)+1);
    if (output_buffer == NULL) return -1;
    struct tvmgen_default_outputs outputs = {
        .output = output_buffer,
    };

    tvmgen_default_run(
        &inputs,
        &outputs
    );

    float* inp_ = (float*) input;
    for (size_t i = 0; i < input_len; i++) {
        printf("INFO (input): %f\n", inp_[i]);
    }

    float* out_hat = (float*) outputs.output;
    float* out_gold = (float*) output;
    for(size_t i = 0; i < output_len; i++) {
        printf("COMP (out_hat, out_gold): (%f, %f)\n", out_hat[i], out_gold[i]);
    }


    free(output_buffer);
    printf("Done.\n");
}