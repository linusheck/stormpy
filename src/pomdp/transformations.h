#pragma once

#include "src/pomdp/common.h"

void define_transformations_nt(py::module &m);
template<typename VT>
void define_transformations(py::module &m);
template<typename VT>
void define_transformations_int(py::module &m);
