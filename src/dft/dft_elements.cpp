#include "dft_elements.h"
#include "src/helpers.h"
#include "storm-dft/storage/dft/DFTElements.h"


template<typename ValueType> using DFTElement = storm::storage::DFTElement<ValueType>;
template<typename ValueType> using BE = storm::storage::DFTBE<ValueType>;
template<typename ValueType> using Dependency = storm::storage::DFTDependency<ValueType>;


template<typename ValueType>
void define_dft_elements(py::module& m, std::string const& vt_suffix) {

    // DFT elements
    py::class_<DFTElement<ValueType>, std::shared_ptr<DFTElement<ValueType>>> element(m, ("DFTElement"+vt_suffix).c_str(), "DFT element");
    element.def_property_readonly("id", &DFTElement<ValueType>::id, "Id")
        .def_property_readonly("name", &DFTElement<ValueType>::name, "Name")
        .def("__str__", &DFTElement<ValueType>::toString)
    ;

    py::class_<BE<ValueType>, std::shared_ptr<BE<ValueType>>>(m, ("DFTBE"+vt_suffix).c_str(), "Basic Event", element)
        .def("__str__", &BE<ValueType>::toString)
    ;

    py::class_<Dependency<ValueType>, std::shared_ptr<Dependency<ValueType>>>(m, ("DFTDependency"+vt_suffix).c_str(), "Dependency", element)
        .def("__str__", &Dependency<ValueType>::toString)
    ;

}


template void define_dft_elements<double>(py::module& m, std::string const& vt_suffix);
template void define_dft_elements<storm::RationalFunction>(py::module& m, std::string const& vt_suffix);
