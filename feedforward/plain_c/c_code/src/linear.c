#include "sml.h"
typedef MATRIX Tensor;
const char* fmt = "%8" SML_PRTREAL "g ";

/**
 * Creates two-dimensional tensor.
*/
Tensor createTensor(REAL* array, size_t Rows, size_t Cols) {   
    Tensor myTensor = MatDim(Rows, Cols) ; 
    for (size_t j = 0; j < Cols; ++j) {
        for (size_t i = 0; i < Rows; ++i) {
            // Access the provided array
            REAL value = array[i * Cols+ j ];
            // Set value in tensor 
            MatSet(myTensor, i + 1, j  + 1, value);
        }
    }
    return myTensor;
}

int main(int argc, char **argv) {
    printf("Executing linear layer:\n\n");

    // DATA ------------------------------------------------------------
    REAL input_data[] = { -0.7658, -0.7506, 1.3525,  0.6863, -0.3278 };

    REAL weights_data[] = {
         0.3419,  0.0902,  0.3887, -0.0631, -0.2060, -0.2062,
        0.3712, -0.2177,  0.0837,  0.3448, -0.0524, -0.1263,
        -0.1048,  0.2626,  0.3304,  0.0661, -0.1816, -0.2689,
        0.4108,  0.3942,  0.0606, -0.2088,  0.2967,  0.0422,
        -0.0980, -0.3281,  0.2156,  0.1140, -0.3530, -0.4417
    };

    REAL bias_data[] = {
        0.4039, -0.3799,  0.3453,  0.0744, -0.1452,  0.2764
    };

    REAL reference_output_data[] = {
        0.0358,  0.4478,  0.4025, -0.2272,  0.1256,  0.3391
    };
    // -----------------------------------------------------------------
    
    // INIT ------------------------------------------------------------
    Tensor input = createTensor(input_data, 1, 5);
    Tensor weights = createTensor(weights_data, 5, 6);
    Tensor bias = createTensor(bias_data, 1, 6);
    Tensor output = MatDim(1, 6);
    Tensor reference_output = createTensor(reference_output_data, 1, 6);
    // -----------------------------------------------------------------

    // RUN -------------------------------------------------------------
    MatMul(output, input, weights);
    MatAdd(output, output, bias);
    // -----------------------------------------------------------------

    // LOG -------------------------------------------------------------
    MatWrite(stdout , input, fmt,"input:");
    MatWrite(stdout , weights, fmt,"weights:");
    MatWrite(stdout , bias, fmt,"bias:");
    MatWrite(stdout , output, fmt,"output:");
    MatWrite(stdout , reference_output, fmt,"reference output:");
    // -----------------------------------------------------------------

}