#pragma once

#include "src/common.h"

template<typename ValueType>
void define_sparse_matrix(py::module& m);

void define_sparse_matrix_nt(py::module& m);
