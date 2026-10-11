#include <carl/core/MonomialPool.h>
#include <carl/core/VariablePool.h>
#include <storm/utility/logging.h>

#include "src/common.h"
#include "src/numbers/valuetype.h"

PYBIND11_MODULE(_numbers, m) {
    m.doc() = "Number types of Storm";

#ifdef STORMPY_DISABLE_SIGNATURE_DOC
    py::options options;
    options.disable_function_signatures();
#endif

    using namespace stormpy::numbers;

    // This module is loaded before the core module and can therefore be the first module loading libstorm.
    // The global state of carl and Storm (variable/monomial pools, root logger) are function-local statics which libstorm does not export as
    // unique symbols. Referencing them here makes this module define them as (GNU-)unique symbols, such that libstorm binds to the instances
    // shared with pycarl and the core module instead of using its own copies (which leads to crashes in parametric model checking).
    carl::VariablePool::getInstance();
    carl::MonomialPool::getInstance();
    l3pp::Logger::getRootLogger();

    define_value_types(m);
}
