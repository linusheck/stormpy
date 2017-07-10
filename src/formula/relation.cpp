#include "relation.h"
#include <carl/formula/Formula.h>

void define_relation(py::module& m) {
    py::enum_<carl::Relation>(m, "Relation")
            .value("EQ", carl::Relation::EQ)
            .value("NEQ", carl::Relation::NEQ)
            .value("LESS", carl::Relation::LESS)
            .value("LEQ", carl::Relation::LEQ)
            .value("GREATER", carl::Relation::GREATER)
            .value("GEQ", carl::Relation::GEQ)
            .def("__str__", [](carl::Relation r) { return carl::relationToString(r); })
            ;
}