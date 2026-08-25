# stormpy public namespace inventory

This is a mechanical inventory of every module-level name that does not begin with `_` in the modules listed below. Inclusion does not mean that a name was intentionally public, documented, or covered by a compatibility guarantee. Class members are not included.

**Total entries:** 931

## Build configuration

| Setting | Value |
|---|---|
| stormpy version | 1.13.2 |
| Python version | 3.12.12 |
| Storm version | 1.14.0 |
| STORM_WITH_DFT | True |
| STORM_WITH_GSPN | True |
| STORM_WITH_PARS | True |
| STORM_WITH_POMDP | True |
| STORM_WITH_SPOT | True |
| STORM_WITH_XERCES | True |

## Review labels

- **KEEP**: retain the public path as-is.
- **ALIAS**: retain it temporarily as an alias to the API named in Target / group.
- **CONSOLIDATE**: combine related specializations under the generic API named in Target / group.
- **DEPRECATE**: begin a deprecation cycle without a direct replacement.
- **PRIVATE**: remove it from the supported public API.

Decision, Target / group, and Notes are the team-editable fields.

## `stormpy`

418 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| CONSOLIDATE | `stormpy.ActionMaskDouble` | class | `stormpy._core` | C++ binding | stormpy.ActionMask | Value-type specialization; expose one Python dispatcher or facade. |
| ALIAS | `stormpy.Add_Sylvan_Double` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Add_Sylvan_Double | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.AddIterator_Sylvan_Double` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.AddIterator_Sylvan_Double | Prefer the domain-oriented import; retain this flattened path during migration. |
| CONSOLIDATE | `stormpy.AddUncertaintyDouble` | class | `stormpy._core` | C++ binding | stormpy.AddUncertainty | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.AddUncertaintyExact` | class | `stormpy._core` | C++ binding | stormpy.AddUncertainty | Value-type specialization; expose one Python dispatcher or facade. |
| ALIAS | `stormpy.ArrayType` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ArrayType | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.AtomicExpressionFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.AtomicExpressionFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.AtomicLabelFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.AtomicLabelFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.BasicType` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.BasicType | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.Bdd_Sylvan` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Bdd_Sylvan | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.BinaryBooleanOperatorType` | enum | `stormpy.logic._logic` | C++ binding | stormpy.logic.BinaryBooleanOperatorType | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.BinaryPathFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.BinaryPathFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.BinaryStateFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.BinaryStateFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.BisimulationOptionsDd` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.BisimulationType` | enum | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.BitVector` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.BitVector | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.BooleanBinaryStateFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.BooleanBinaryStateFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.BooleanLiteralFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.BooleanLiteralFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.BoundedType` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.BoundedType | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.BoundedUntilFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.BoundedUntilFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.build_exact_interval_model_from_drn` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.build_from_umb` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.build_interval_model_from_drn` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.build_model` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.build_model_from_drn` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.build_parametric_model` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.build_parametric_model_from_drn` | function | `stormpy` | Python |  |  |
| ALIAS | `stormpy.build_parametric_sparse_matrix` | function | `stormpy.storage` | Python | stormpy.storage.build_parametric_sparse_matrix | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.build_sparse_exact_interval_model` | function | `stormpy` | Python |  |  |
| CONSOLIDATE | `stormpy.build_sparse_exact_interval_model_with_options` | function | `stormpy._core` | C++ binding | stormpy.build_sparse_model_with_options | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.build_sparse_exact_model` | function | `stormpy` | Python |  |  |
| CONSOLIDATE | `stormpy.build_sparse_exact_model_with_options` | function | `stormpy._core` | C++ binding | stormpy.build_sparse_model_with_options | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.build_sparse_interval_model` | function | `stormpy` | Python |  |  |
| CONSOLIDATE | `stormpy.build_sparse_interval_model_with_options` | function | `stormpy._core` | C++ binding | stormpy.build_sparse_model_with_options | Value-type specialization; expose one Python dispatcher or facade. |
| ALIAS | `stormpy.build_sparse_matrix` | function | `stormpy.storage` | Python | stormpy.storage.build_sparse_matrix | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.build_sparse_model` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.build_sparse_model_from_explicit` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.build_sparse_model_with_options` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.build_sparse_parametric_model` | function | `stormpy` | Python |  |  |
| CONSOLIDATE | `stormpy.build_sparse_parametric_model_with_options` | function | `stormpy._core` | C++ binding | stormpy.build_sparse_model_with_options | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.build_symbolic_model` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.build_symbolic_parametric_model` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.BuilderOptions` | class | `stormpy._core` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.check_exact_interval_dtmc` | function | `stormpy._core` | C++ binding | stormpy.check_dtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.check_exact_interval_mdp` | function | `stormpy._core` | C++ binding | stormpy.check_mdp | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.check_interval_dtmc` | function | `stormpy._core` | C++ binding | stormpy.check_dtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.check_interval_mdp` | function | `stormpy._core` | C++ binding | stormpy.check_mdp | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.check_model_dd` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.check_model_hybrid` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.check_model_sparse` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.CheckTask` | class | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.ChoiceLabeling` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ChoiceLabeling | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ChoiceOrigins` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ChoiceOrigins | Prefer the domain-oriented import; retain this flattened path during migration. |
| PRIVATE | `stormpy.cln` | module | `stormpy.pycarl.cln` | Python | stormpy.pycarl.cln | Imported implementation/helper module; do not expose as API. |
| ALIAS | `stormpy.ClockType` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ClockType | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.collect_information` | function | `stormpy.storage._storage` | C++ binding | stormpy.storage.collect_information | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ComparisonType` | enum | `stormpy.logic._logic` | C++ binding | stormpy.logic.ComparisonType | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.CompressionMode` | enum | `stormpy.storage._storage` | C++ binding | stormpy.storage.CompressionMode | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.compute_all_until_probabilities` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.compute_expected_number_of_visits` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.compute_prob01_states` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.compute_prob01max_states` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.compute_prob01min_states` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.compute_steady_state_distribution` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.compute_transient_probabilities` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.ConditionalAlgorithmSetting` | enum | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.ConditionalFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.ConditionalFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.ConditionalModelCheckerEnvironment` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.ConstraintCollector` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.construct_submodel` | function | `stormpy` | Python |  |  |
| ALIAS | `stormpy.ContinuousType` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ContinuousType | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.create_filter_initial_states_sparse` | function | `stormpy._core` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.create_filter_initial_states_sparseExact` | function | `stormpy._core` | C++ binding | stormpy.create_filter_initial_states_sparse | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.create_filter_initial_states_symbolic` | function | `stormpy._core` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.create_filter_initial_states_symbolicExact` | function | `stormpy._core` | C++ binding | stormpy.create_filter_initial_states_symbolic | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.create_filter_symbolic` | function | `stormpy._core` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.create_filter_symbolicExact` | function | `stormpy._core` | C++ binding | stormpy.create_filter_symbolic | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.CuddDdManagerEnvironment` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.CuddReorderingTechnique` | enum | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.CumulativeRewardFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.CumulativeRewardFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.Dd_Sylvan` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Dd_Sylvan | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.DdEnvironment` | class | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.DdManager_Sylvan` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.DdManager_Sylvan | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.DdMetaVariable_Sylvan` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.DdMetaVariable_Sylvan | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.DdMetaVariableType` | enum | `stormpy.storage._storage` | C++ binding | stormpy.storage.DdMetaVariableType | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.deprecated` | function | `deprecated.sphinx` | external | stormpy.storage.deprecated | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.DiceStringVisitor` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.DiceStringVisitor | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.DirectEncodingExporterOptions` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.DirectEncodingParserOptions` | class | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.Distribution` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Distribution | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.DistributionExact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.DistributionExact | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.DistributionInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.DistributionInterval | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.DistributionRationalInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.DistributionRationalInterval | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.eliminate_ECs` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.eliminate_non_markovian_chains` | function | `stormpy` | Python |  |  |
| ALIAS | `stormpy.eliminate_reward_accumulations` | function | `stormpy.storage._storage` | C++ binding | stormpy.storage.eliminate_reward_accumulations | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.EliminationLabelBehavior` | enum | `stormpy._core` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.EndComponentEliminatorReturnTypeDouble` | class | `stormpy._core` | C++ binding | stormpy.EndComponentEliminatorReturnType | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.EndComponentEliminatorReturnTypeExact` | class | `stormpy._core` | C++ binding | stormpy.EndComponentEliminatorReturnType | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.EndComponentEliminatorReturnTypeInterval` | class | `stormpy._core` | C++ binding | stormpy.EndComponentEliminatorReturnType | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.EndComponentEliminatorReturnTypeRatFunc` | class | `stormpy._core` | C++ binding | stormpy.EndComponentEliminatorReturnType | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.EndComponentEliminatorReturnTypeRationalInterval` | class | `stormpy._core` | C++ binding | stormpy.EndComponentEliminatorReturnType | Value-type specialization; expose one Python dispatcher or facade. |
| PRIVATE | `stormpy.Enum` | enum | `enum` | external |  | Accidentally imported external helper; not stormpy API. |
| KEEP | `stormpy.Environment` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.EquationSolverType` | enum | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.EventuallyFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.EventuallyFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| CONSOLIDATE | `stormpy.ExactCheckTask` | class | `stormpy._core` | C++ binding | stormpy.CheckTask | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.ExactParetoCurveCheckResult` | class | `stormpy._core` | C++ binding | stormpy.ParetoCurveCheckResult | Value-type specialization; expose one Python dispatcher or facade. |
| ALIAS | `stormpy.ExactSparseMatrix` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ExactSparseMatrix | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ExactSparseMatrixBuilder` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ExactSparseMatrixBuilder | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ExactSparseMatrixEntry` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ExactSparseMatrixEntry | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ExactSparseMatrixRows` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ExactSparseMatrixRows | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.exceptions` | module | `stormpy.exceptions` | Python |  |  |
| CONSOLIDATE | `stormpy.ExplicitExactIntervalModelBuilderOptions` | class | `stormpy._core` | C++ binding | stormpy.ExplicitModelBuilderOptions | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.ExplicitExactModelBuilderOptions` | class | `stormpy._core` | C++ binding | stormpy.ExplicitModelBuilderOptions | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.ExplicitExactParetoCurveCheckResult` | class | `stormpy._core` | C++ binding | stormpy.ExplicitParetoCurveCheckResult | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.ExplicitExactQualitativeCheckResult` | class | `stormpy._core` | C++ binding | stormpy.ExplicitQualitativeCheckResult | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.ExplicitExactQuantitativeCheckResult` | class | `stormpy._core` | C++ binding | stormpy.ExplicitQuantitativeCheckResult | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.ExplicitIntervalModelBuilderOptions` | class | `stormpy._core` | C++ binding | stormpy.ExplicitModelBuilderOptions | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.ExplicitModelBuilder` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.ExplicitModelBuilderOptions` | class | `stormpy._core` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.ExplicitModelCheckerHintDouble` | class | `stormpy._core` | C++ binding | stormpy.ExplicitModelCheckerHint | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.ExplicitModelParserOptions` | class | `stormpy._core` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.ExplicitParametricModelBuilder` | class | `stormpy._core` | C++ binding | stormpy.ExplicitModelBuilder | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.ExplicitParametricModelBuilderOptions` | class | `stormpy._core` | C++ binding | stormpy.ExplicitModelBuilderOptions | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.ExplicitParametricQualitativeCheckResult` | class | `stormpy._core` | C++ binding | stormpy.ExplicitQualitativeCheckResult | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.ExplicitParametricQuantitativeCheckResult` | class | `stormpy._core` | C++ binding | stormpy.ExplicitQuantitativeCheckResult | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.ExplicitParetoCurveCheckResult` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.ExplicitQualitativeCheckResult` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.ExplicitQuantitativeCheckResult` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.ExplicitStateLookup` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.ExplorationOrder` | enum | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.export_jani_to_file` | function | `stormpy.storage._storage` | C++ binding | stormpy.storage.export_jani_to_file | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.export_to_drn` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.export_to_umb` | function | `stormpy` | Python |  |  |
| ALIAS | `stormpy.Expression` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Expression | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ExpressionManager` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ExpressionManager | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ExpressionParser` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ExpressionParser | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ExpressionType` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ExpressionType | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.FactorizedPolynomial` | class | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.FactorizedRationalFunction` | class | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.FlatSet` | class | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.Formula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.Formula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.GameFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.GameFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.get_maximal_end_components` | function | `stormpy.storage` | Python | stormpy.storage.get_maximal_end_components | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.get_reachable_states` | function | `stormpy` | Python |  |  |
| ALIAS | `stormpy.GloballyFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.GloballyFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| PRIVATE | `stormpy.gmp` | module | `stormpy.pycarl.gmp` | Python | stormpy.pycarl.gmp | Imported implementation/helper module; do not expose as API. |
| CONSOLIDATE | `stormpy.HybridExactQuantitativeCheckResult` | class | `stormpy._core` | C++ binding | stormpy.HybridQuantitativeCheckResult | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.HybridParametricQuantitativeCheckResult` | class | `stormpy._core` | C++ binding | stormpy.HybridQuantitativeCheckResult | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.HybridQuantitativeCheckResult` | class | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.import_umb` | function | `stormpy.storage._storage` | C++ binding | stormpy.storage.import_umb | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.install_signal_handlers` | function | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.InstantaneousRewardFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.InstantaneousRewardFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.IntervalSparseMatrix` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.IntervalSparseMatrix | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.IntervalSparseMatrixBuilder` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.IntervalSparseMatrixBuilder | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.IntervalSparseMatrixEntry` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.IntervalSparseMatrixEntry | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.IntervalSparseMatrixRows` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.IntervalSparseMatrixRows | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ItemLabeling` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ItemLabeling | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniAssignment` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniAssignment | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniAutomaton` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniAutomaton | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniChoiceOrigins` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniChoiceOrigins | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniConstant` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniConstant | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniEdge` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniEdge | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniEdgeDestination` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniEdgeDestination | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniInformationObject` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniInformationObject | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniLocation` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniLocation | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniLocationExpander` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniLocationExpander | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniModel | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.JaniModelType` | enum | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.JaniOrderedAssignments` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniOrderedAssignments | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniScopeChanger` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniScopeChanger | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniTemplateEdge` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniTemplateEdge | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniTemplateEdgeDestination` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniTemplateEdgeDestination | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniType` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniType | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniVariable` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniVariable | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.JaniVariableSet` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.JaniVariableSet | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.logic` | module | `stormpy.logic` | Python |  |  |
| ALIAS | `stormpy.LongRunAvarageOperator` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.LongRunAvarageOperator | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.LongRunAverageRewardFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.LongRunAverageRewardFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.make_sparse_model_builder` | function | `stormpy._core` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.make_sparse_model_builder_exact` | function | `stormpy._core` | C++ binding | stormpy.make_sparse_model_builder | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.make_sparse_model_builder_parametric` | function | `stormpy._core` | C++ binding | stormpy.make_sparse_model_builder | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.make_weighted_objective_mdp_model_checker` | function | `stormpy` | Python |  |  |
| ALIAS | `stormpy.MaximalEndComponent` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MaximalEndComponent | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MaximalEndComponentDecomposition_double` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MaximalEndComponentDecomposition_double | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MaximalEndComponentDecomposition_exact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MaximalEndComponentDecomposition_exact | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MaximalEndComponentDecomposition_interval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MaximalEndComponentDecomposition_interval | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MaximalEndComponentDecomposition_ratfunc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MaximalEndComponentDecomposition_ratfunc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MaximalEndComponentDecomposition_ratinterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MaximalEndComponentDecomposition_ratinterval | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MemoryStructure` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructure | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MemoryStructureBuilder` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureBuilder | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MemoryStructureBuilderExact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureBuilderExact | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MemoryStructureBuilderInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureBuilderInterval | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MemoryStructureBuilderParametric` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureBuilderParametric | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MemoryStructureProduct` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureProduct | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MemoryStructureProductExact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureProductExact | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MemoryStructureProductInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureProductInterval | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.MemoryStructureProductParametric` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureProductParametric | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.MinMaxMethod` | enum | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.MinMaxSolverEnvironment` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.model_checking` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.ModelCheckerEnvironment` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.ModelCheckerHint` | class | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.ModelType` | enum | `stormpy.storage._storage` | C++ binding | stormpy.storage.ModelType | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.MultiObjectiveEncodingType` | enum | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.MultiObjectiveFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.MultiObjectiveFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.MultiObjectiveMethod` | enum | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.MultiObjectiveModelCheckerEnvironment` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.MultiObjectivePrecisionType` | enum | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.NativeLinearEquationSolverMethod` | enum | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.NativeSolverEnvironment` | class | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.OperatorFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.OperatorFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.OperatorType` | enum | `stormpy.storage._storage` | C++ binding | stormpy.storage.OperatorType | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.OptimizationDirection` | enum | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.OverlappingGuardAnalyser` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.OverlappingGuardAnalyser | Prefer the domain-oriented import; retain this flattened path during migration. |
| CONSOLIDATE | `stormpy.ParametricCheckTask` | class | `stormpy._core` | C++ binding | stormpy.CheckTask | Value-type specialization; expose one Python dispatcher or facade. |
| ALIAS | `stormpy.ParametricSparseMatrix` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ParametricSparseMatrix | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ParametricSparseMatrixBuilder` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ParametricSparseMatrixBuilder | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ParametricSparseMatrixEntry` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ParametricSparseMatrixEntry | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ParametricSparseMatrixRows` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ParametricSparseMatrixRows | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.ParetoCurveCheckResult` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.parse_constants_string` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.parse_jani_model` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.parse_jani_model_from_string` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.parse_prism_program` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.parse_properties` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.parse_properties_for_jani_model` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.parse_properties_for_prism_program` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.parse_properties_without_context` | function | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.PathFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.PathFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.perform_bisimulation` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.perform_sparse_bisimulation` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.perform_symbolic_bisimulation` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.Polynomial` | class | `stormpy.pycarl.cln` | Python |  |  |
| ALIAS | `stormpy.PolytopeDouble` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PolytopeDouble | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PolytopeExact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PolytopeExact | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.preprocess_symbolic_input` | function | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.PrismAssignment` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismAssignment | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PrismBooleanVariable` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismBooleanVariable | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PrismChoiceOrigins` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismChoiceOrigins | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PrismCommand` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismCommand | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PrismConstant` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismConstant | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PrismIntegerVariable` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismIntegerVariable | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PrismLabel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismLabel | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PrismModelType` | enum | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismModelType | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PrismModule` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismModule | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PrismProgram` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismProgram | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PrismRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismRewardModel | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PrismUpdate` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismUpdate | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.PrismVariable` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.PrismVariable | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.prob01max_states` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.prob01min_states` | function | `stormpy` | Python |  |  |
| ALIAS | `stormpy.ProbabilityOperator` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.ProbabilityOperator | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.product_model` | function | `stormpy.storage` | Python | stormpy.storage.product_model | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.Property` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl` | module | `stormpy.pycarl` | Python |  |  |
| KEEP | `stormpy.QuotientFormat` | enum | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.Rational` | class | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.RationalFunction` | class | `stormpy.pycarl.cln` | Python |  |  |
| ALIAS | `stormpy.RationalIntervalSparseMatrix` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.RationalIntervalSparseMatrix | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.RationalIntervalSparseMatrixBuilder` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.RationalIntervalSparseMatrixBuilder | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.RationalIntervalSparseMatrixEntry` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.RationalIntervalSparseMatrixEntry | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.RationalIntervalSparseMatrixRows` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.RationalIntervalSparseMatrixRows | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.RationalRF` | class | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.reset_timeout` | function | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.RewardOperator` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.RewardOperator | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.Scheduler` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Scheduler | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SchedulerChoice` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerChoice | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SchedulerChoiceExact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerChoiceExact | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SchedulerChoiceInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerChoiceInterval | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SchedulerChoiceParametric` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerChoiceParametric | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SchedulerChoiceRationalInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerChoiceRationalInterval | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.SchedulerClass` | class | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.SchedulerExact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerExact | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SchedulerInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerInterval | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.SchedulerMemoryPattern` | enum | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.SchedulerParametric` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerParametric | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SchedulerRationalInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerRationalInterval | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.set_loglevel_debug` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.set_loglevel_error` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.set_loglevel_trace` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.set_settings` | function | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.set_state_valuations` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.set_timeout` | function | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.SimpleValuation` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SimpleValuation | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.SMTCounterExampleGenerator` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.SMTCounterExampleGeneratorOptions` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.SMTCounterExampleGeneratorStats` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.SMTCounterExampleInput` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.SolverEnvironment` | class | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.sparse_model_from_umb` | function | `stormpy.storage._storage` | C++ binding | stormpy.storage.sparse_model_from_umb | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.sparse_model_to_umb` | function | `stormpy.storage._storage` | C++ binding | stormpy.storage.sparse_model_to_umb | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseCtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseDtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseExactCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseExactCtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseExactDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseExactDtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseExactMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseExactMA | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseExactMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseExactMdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseExactModelAction` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseExactModelAction | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseExactModelActions` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseExactModelActions | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseExactModelComponents` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseExactModelComponents | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseExactModelState` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseExactModelState | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseExactModelStates` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseExactModelStates | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseExactPomdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseExactPomdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseExactRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseExactRewardModel | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseExactSmg` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseExactSmg | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseIntervalCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseIntervalCtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseIntervalDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseIntervalDtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseIntervalMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseIntervalMA | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseIntervalMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseIntervalMdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseIntervalModelAction` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseIntervalModelAction | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseIntervalModelActions` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseIntervalModelActions | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseIntervalModelComponents` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseIntervalModelComponents | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseIntervalModelState` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseIntervalModelState | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseIntervalModelStates` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseIntervalModelStates | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseIntervalPomdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseIntervalPomdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseIntervalRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseIntervalRewardModel | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseIntervalSmg` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseIntervalSmg | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMA | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseMatrix` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrix | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseMatrixBuilder` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixBuilder | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseMatrixEntry` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixEntry | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseMatrixRows` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixRows | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseModelAction` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelAction | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseModelActions` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelActions | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseModelComponents` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelComponents | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseModelMemoryProductReverseData` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelMemoryProductReverseData | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseModelState` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelState | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseModelStates` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelStates | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseParametricCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseParametricCtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseParametricDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseParametricDtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseParametricMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseParametricMA | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseParametricMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseParametricMdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseParametricModelAction` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseParametricModelAction | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseParametricModelActions` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseParametricModelActions | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseParametricModelComponents` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseParametricModelComponents | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseParametricModelState` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseParametricModelState | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseParametricModelStates` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseParametricModelStates | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseParametricPomdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseParametricPomdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseParametricRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseParametricRewardModel | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseParametricSmg` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseParametricSmg | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparsePomdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparsePomdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRationalIntervalCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRationalIntervalCtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRationalIntervalDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRationalIntervalDtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRationalIntervalMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRationalIntervalMA | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRationalIntervalMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRationalIntervalMdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRationalIntervalModelAction` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRationalIntervalModelAction | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRationalIntervalModelActions` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRationalIntervalModelActions | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRationalIntervalModelComponents` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRationalIntervalModelComponents | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRationalIntervalModelState` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRationalIntervalModelState | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRationalIntervalModelStates` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRationalIntervalModelStates | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRationalIntervalPomdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRationalIntervalPomdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRationalIntervalRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRationalIntervalRewardModel | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRationalIntervalSmg` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRationalIntervalSmg | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRewardModel | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SparseSmg` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseSmg | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.StateFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.StateFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.StateLabeling` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.StateLabeling | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.StateValuation` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.StateValuation | Prefer the domain-oriented import; retain this flattened path during migration. |
| CONSOLIDATE | `stormpy.StateValuationFunctionActionMaskDouble` | class | `stormpy._core` | C++ binding | stormpy.StateValuationFunctionActionMask | Value-type specialization; expose one Python dispatcher or facade. |
| ALIAS | `stormpy.StateValuationsBuilder` | class | `stormpy.storage` | Python | stormpy.storage.StateValuationsBuilder | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.StateValuationTransformer` | class | `stormpy.storage` | Python | stormpy.storage.StateValuationTransformer | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.SteadyStateDistributionAlgorithm` | enum | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.storage` | module | `stormpy.storage` | Python |  |  |
| ALIAS | `stormpy.stormpy` | module | `stormpy` | Python | stormpy.storage.stormpy | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.SubsystemBuilderOptions` | class | `stormpy._core` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.SubsystemBuilderReturnTypeDouble` | class | `stormpy._core` | C++ binding | stormpy.SubsystemBuilderReturnType | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.SubsystemBuilderReturnTypeExact` | class | `stormpy._core` | C++ binding | stormpy.SubsystemBuilderReturnType | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.SubsystemBuilderReturnTypeInterval` | class | `stormpy._core` | C++ binding | stormpy.SubsystemBuilderReturnType | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.SubsystemBuilderReturnTypeRatFunc` | class | `stormpy._core` | C++ binding | stormpy.SubsystemBuilderReturnType | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.SubsystemBuilderReturnTypeRationalInterval` | class | `stormpy._core` | C++ binding | stormpy.SubsystemBuilderReturnType | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.SylvanDdManagerEnvironment` | class | `stormpy._core` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.SymbolicExactQuantitativeCheckResult` | class | `stormpy._core` | C++ binding | stormpy.SymbolicQuantitativeCheckResult | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.SymbolicModelDescription` | class | `stormpy._core` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.SymbolicParametricQuantitativeCheckResult` | class | `stormpy._core` | C++ binding | stormpy.SymbolicQuantitativeCheckResult | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.SymbolicQualitativeCheckResult` | class | `stormpy._core` | C++ binding |  |  |
| KEEP | `stormpy.SymbolicQuantitativeCheckResult` | class | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.SymbolicSylvanCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanCtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanDtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanExactCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanExactCtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanExactDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanExactDtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanExactMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanExactMA | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanExactMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanExactMdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanExactRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanExactRewardModel | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanMA | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanMdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanParametricCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanParametricCtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanParametricDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanParametricDtmc | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanParametricMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanParametricMA | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanParametricMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanParametricMdp | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanParametricRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanParametricRewardModel | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.SymbolicSylvanRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanRewardModel | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.TimeOperator` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.TimeOperator | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.topological_sort` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.transform_to_discrete_time_model` | function | `stormpy` | Python |  |  |
| KEEP | `stormpy.transform_to_sparse_model` | function | `stormpy` | Python |  |  |
| ALIAS | `stormpy.umb_to_archive` | function | `stormpy.storage._storage` | C++ binding | stormpy.storage.umb_to_archive | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.UmbExportOptions` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.UmbExportOptions | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.UmbExportValueType` | enum | `stormpy.storage._storage` | C++ binding | stormpy.storage.UmbExportValueType | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.UmbImportOptions` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.UmbImportOptions | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.UmbImportValueType` | enum | `stormpy.storage._storage` | C++ binding | stormpy.storage.UmbImportValueType | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.UmbModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.UmbModel | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.UnaryBooleanStateFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.UnaryBooleanStateFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.UnaryPathFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.UnaryPathFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.UnaryStateFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.UnaryStateFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.UncertaintyResolutionMode` | enum | `stormpy._core` | C++ binding |  |  |
| ALIAS | `stormpy.UntilFormula` | class | `stormpy.logic._logic` | C++ binding | stormpy.logic.UntilFormula | Prefer the domain-oriented import; retain this flattened path during migration. |
| KEEP | `stormpy.utility` | module | `stormpy.utility` | Python |  |  |
| ALIAS | `stormpy.Valuation` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Valuation | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ValuationClassDescription` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ValuationClassDescription | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ValuationDescriptionBuilder` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ValuationDescriptionBuilder | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.Valuations` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Valuations | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.ValuationTransformer` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.ValuationTransformer | Prefer the domain-oriented import; retain this flattened path during migration. |
| ALIAS | `stormpy.Variable` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Variable | Prefer the domain-oriented import; retain this flattened path during migration. |
| CONSOLIDATE | `stormpy.WeightedObjectiveMdpModelCheckerDouble` | class | `stormpy._core` | C++ binding | stormpy.WeightedObjectiveMdpModelChecker | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.WeightedObjectiveMdpModelCheckerExact` | class | `stormpy._core` | C++ binding | stormpy.WeightedObjectiveMdpModelChecker | Value-type specialization; expose one Python dispatcher or facade. |

## `stormpy.storage`

211 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| CONSOLIDATE | `stormpy.storage.Add_Sylvan_Double` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Add_Sylvan | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.AddIterator_Sylvan_Double` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.AddIterator_Sylvan | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.ArrayType` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.BasicType` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.Bdd_Sylvan` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.BitVector` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.BoundedType` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.build_parametric_sparse_matrix` | function | `stormpy.storage` | Python |  |  |
| KEEP | `stormpy.storage.build_sparse_matrix` | function | `stormpy.storage` | Python |  |  |
| KEEP | `stormpy.storage.ChoiceLabeling` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.ChoiceOrigins` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.ClockType` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.collect_information` | function | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.CompressionMode` | enum | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.ContinuousType` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.Dd_Sylvan` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.DdManager_Sylvan` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.DdMetaVariable_Sylvan` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.DdMetaVariableType` | enum | `stormpy.storage._storage` | C++ binding |  |  |
| PRIVATE | `stormpy.storage.deprecated` | function | `deprecated.sphinx` | external |  | Accidentally imported external helper; not stormpy API. |
| KEEP | `stormpy.storage.DiceStringVisitor` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.Distribution` | class | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.DistributionExact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Distribution | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.DistributionInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Distribution | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.DistributionRationalInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Distribution | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.eliminate_reward_accumulations` | function | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.ExactSparseMatrix` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrix | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.ExactSparseMatrixBuilder` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixBuilder | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.ExactSparseMatrixEntry` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixEntry | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.ExactSparseMatrixRows` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixRows | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.export_jani_to_file` | function | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.Expression` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.ExpressionManager` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.ExpressionParser` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.ExpressionType` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.get_maximal_end_components` | function | `stormpy.storage` | Python |  |  |
| KEEP | `stormpy.storage.import_umb` | function | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.IntervalSparseMatrix` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrix | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.IntervalSparseMatrixBuilder` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixBuilder | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.IntervalSparseMatrixEntry` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixEntry | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.IntervalSparseMatrixRows` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixRows | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.ItemLabeling` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniAssignment` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniAutomaton` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniChoiceOrigins` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniConstant` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniEdge` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniEdgeDestination` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniInformationObject` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniLocation` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniLocationExpander` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniModel` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniOrderedAssignments` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniScopeChanger` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniTemplateEdge` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniTemplateEdgeDestination` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniType` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniVariable` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.JaniVariableSet` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.MaximalEndComponent` | class | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.MaximalEndComponentDecomposition_double` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MaximalEndComponentDecomposition | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.MaximalEndComponentDecomposition_exact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MaximalEndComponentDecomposition | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.MaximalEndComponentDecomposition_interval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MaximalEndComponentDecomposition | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.MaximalEndComponentDecomposition_ratfunc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MaximalEndComponentDecomposition | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.MaximalEndComponentDecomposition_ratinterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MaximalEndComponentDecomposition | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.MemoryStructure` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.MemoryStructureBuilder` | class | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.MemoryStructureBuilderExact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureBuilder | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.MemoryStructureBuilderInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureBuilder | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.MemoryStructureBuilderParametric` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureBuilder | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.MemoryStructureProduct` | class | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.MemoryStructureProductExact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureProduct | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.MemoryStructureProductInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureProduct | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.MemoryStructureProductParametric` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.MemoryStructureProduct | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.ModelType` | enum | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.OperatorType` | enum | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.OverlappingGuardAnalyser` | class | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.ParametricSparseMatrix` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrix | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.ParametricSparseMatrixBuilder` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixBuilder | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.ParametricSparseMatrixEntry` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixEntry | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.ParametricSparseMatrixRows` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixRows | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.PolytopeDouble` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Polytope | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.PolytopeExact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Polytope | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.PrismAssignment` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.PrismBooleanVariable` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.PrismChoiceOrigins` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.PrismCommand` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.PrismConstant` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.PrismIntegerVariable` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.PrismLabel` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.PrismModelType` | enum | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.PrismModule` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.PrismProgram` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.PrismRewardModel` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.PrismUpdate` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.PrismVariable` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.product_model` | function | `stormpy.storage` | Python |  |  |
| CONSOLIDATE | `stormpy.storage.RationalIntervalSparseMatrix` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrix | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.RationalIntervalSparseMatrixBuilder` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixBuilder | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.RationalIntervalSparseMatrixEntry` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixEntry | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.RationalIntervalSparseMatrixRows` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMatrixRows | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.Scheduler` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SchedulerChoice` | class | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.SchedulerChoiceExact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerChoice | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SchedulerChoiceInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerChoice | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SchedulerChoiceParametric` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerChoice | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SchedulerChoiceRationalInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SchedulerChoice | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SchedulerExact` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Scheduler | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SchedulerInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Scheduler | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SchedulerParametric` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Scheduler | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SchedulerRationalInterval` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.Scheduler | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.SimpleValuation` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.sparse_model_from_umb` | function | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.sparse_model_to_umb` | function | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseCtmc` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseDtmc` | class | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.SparseExactCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseCtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseExactDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseDtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseExactMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMA | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseExactMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMdp | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseExactModelAction` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelAction | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseExactModelActions` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelActions | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseExactModelComponents` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelComponents | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseExactModelState` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelState | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseExactModelStates` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelStates | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseExactPomdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparsePomdp | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseExactRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRewardModel | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseExactSmg` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseSmg | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseIntervalCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseCtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseIntervalDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseDtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseIntervalMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMA | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseIntervalMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMdp | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseIntervalModelAction` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelAction | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseIntervalModelActions` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelActions | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseIntervalModelComponents` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelComponents | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseIntervalModelState` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelState | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseIntervalModelStates` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelStates | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseIntervalPomdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparsePomdp | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseIntervalRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRewardModel | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseIntervalSmg` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseSmg | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.SparseMA` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseMatrix` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseMatrixBuilder` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseMatrixEntry` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseMatrixRows` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseMdp` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseModelAction` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseModelActions` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseModelComponents` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseModelMemoryProductReverseData` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseModelState` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseModelStates` | class | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.SparseParametricCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseCtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseParametricDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseDtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseParametricMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMA | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseParametricMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMdp | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseParametricModelAction` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelAction | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseParametricModelActions` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelActions | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseParametricModelComponents` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelComponents | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseParametricModelState` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelState | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseParametricModelStates` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelStates | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseParametricPomdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparsePomdp | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseParametricRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRewardModel | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseParametricSmg` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseSmg | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.SparsePomdp` | class | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.SparseRationalIntervalCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseCtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseRationalIntervalDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseDtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseRationalIntervalMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMA | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseRationalIntervalMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseMdp | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseRationalIntervalModelAction` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelAction | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseRationalIntervalModelActions` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelActions | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseRationalIntervalModelComponents` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelComponents | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseRationalIntervalModelState` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelState | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseRationalIntervalModelStates` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseModelStates | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseRationalIntervalPomdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparsePomdp | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseRationalIntervalRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseRewardModel | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SparseRationalIntervalSmg` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SparseSmg | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.SparseRewardModel` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SparseSmg` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.StateLabeling` | class | `stormpy.storage._storage` | C++ binding |  |  |
| DEPRECATE | `stormpy.storage.StateValuation` | class | `stormpy.storage._storage` | C++ binding |  | Already deprecated or retained as a legacy compatibility shim. |
| DEPRECATE | `stormpy.storage.StateValuationsBuilder` | class | `stormpy.storage` | Python |  | Already deprecated or retained as a legacy compatibility shim. |
| DEPRECATE | `stormpy.storage.StateValuationTransformer` | class | `stormpy.storage` | Python |  | Already deprecated or retained as a legacy compatibility shim. |
| PRIVATE | `stormpy.storage.stormpy` | module | `stormpy` | Python |  | Imported implementation/helper module; do not expose as API. |
| KEEP | `stormpy.storage.SymbolicSylvanCtmc` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SymbolicSylvanDtmc` | class | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.SymbolicSylvanExactCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanCtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SymbolicSylvanExactDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanDtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SymbolicSylvanExactMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanMA | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SymbolicSylvanExactMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanMdp | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SymbolicSylvanExactRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanRewardModel | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.SymbolicSylvanMA` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.SymbolicSylvanMdp` | class | `stormpy.storage._storage` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.storage.SymbolicSylvanParametricCtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanCtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SymbolicSylvanParametricDtmc` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanDtmc | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SymbolicSylvanParametricMA` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanMA | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SymbolicSylvanParametricMdp` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanMdp | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.storage.SymbolicSylvanParametricRewardModel` | class | `stormpy.storage._storage` | C++ binding | stormpy.storage.SymbolicSylvanRewardModel | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.storage.SymbolicSylvanRewardModel` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.umb_to_archive` | function | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.UmbExportOptions` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.UmbExportValueType` | enum | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.UmbImportOptions` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.UmbImportValueType` | enum | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.UmbModel` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.Valuation` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.ValuationClassDescription` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.ValuationDescriptionBuilder` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.Valuations` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.ValuationTransformer` | class | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.storage.Variable` | class | `stormpy.storage._storage` | C++ binding |  |  |

## `stormpy.logic`

29 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.logic.AtomicExpressionFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.AtomicLabelFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.BinaryBooleanOperatorType` | enum | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.BinaryPathFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.BinaryStateFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.BooleanBinaryStateFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.BooleanLiteralFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.BoundedUntilFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.ComparisonType` | enum | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.ConditionalFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.CumulativeRewardFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.EventuallyFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.Formula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.GameFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.GloballyFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.InstantaneousRewardFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.LongRunAvarageOperator` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.LongRunAverageRewardFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.MultiObjectiveFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.OperatorFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.PathFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.ProbabilityOperator` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.RewardOperator` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.StateFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.TimeOperator` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.UnaryBooleanStateFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.UnaryPathFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.UnaryStateFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |
| KEEP | `stormpy.logic.UntilFormula` | class | `stormpy.logic._logic` | C++ binding |  |  |

## `stormpy.utility`

13 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| CONSOLIDATE | `stormpy.utility.JsonContainerDouble` | class | `stormpy.utility._utility` | C++ binding | stormpy.utility.JsonContainer | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.utility.JsonContainerRational` | class | `stormpy.utility._utility` | C++ binding |  |  |
| KEEP | `stormpy.utility.MatrixFormat` | enum | `stormpy.utility._utility` | C++ binding |  |  |
| KEEP | `stormpy.utility.milliseconds` | class | `stormpy.utility._utility` | C++ binding |  |  |
| KEEP | `stormpy.utility.ModelReference` | class | `stormpy.utility._utility` | C++ binding |  |  |
| KEEP | `stormpy.utility.Path` | class | `stormpy.utility._utility` | C++ binding |  |  |
| KEEP | `stormpy.utility.sharpen` | function | `stormpy.utility._utility` | C++ binding |  |  |
| KEEP | `stormpy.utility.ShortestPathsGenerator` | class | `stormpy.utility._utility` | C++ binding |  |  |
| KEEP | `stormpy.utility.SmtCheckResult` | enum | `stormpy.utility._utility` | C++ binding |  |  |
| KEEP | `stormpy.utility.SmtSolver` | class | `stormpy.utility._utility` | C++ binding |  |  |
| KEEP | `stormpy.utility.SmtSolverFactory` | class | `stormpy.utility._utility` | C++ binding |  |  |
| KEEP | `stormpy.utility.Z3SmtSolver` | class | `stormpy.utility._utility` | C++ binding |  |  |
| KEEP | `stormpy.utility.Z3SmtSolverFactory` | class | `stormpy.utility._utility` | C++ binding |  |  |

## `stormpy.utility.multiobjective_plotting` (optional: plot dependencies)

4 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| PRIVATE | `stormpy.utility.multiobjective_plotting.np` | module | `numpy` | external |  | Imported implementation/helper module; do not expose as API. |
| KEEP | `stormpy.utility.multiobjective_plotting.plot_convex_pareto_curve_demo` | function | `stormpy.utility.multiobjective_plotting` | Python |  |  |
| KEEP | `stormpy.utility.multiobjective_plotting.prepare_multiobjective_result_for_plotting` | function | `stormpy.utility.multiobjective_plotting` | Python |  |  |
| PRIVATE | `stormpy.utility.multiobjective_plotting.stormpy` | module | `stormpy` | Python |  | Imported implementation/helper module; do not expose as API. |

## `stormpy.simulator`

8 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.simulator.create_simulator` | function | `stormpy.simulator` | Python |  |  |
| PRIVATE | `stormpy.simulator.Enum` | enum | `enum` | external |  | Accidentally imported external helper; not stormpy API. |
| KEEP | `stormpy.simulator.PrismSimulator` | class | `stormpy.simulator` | Python |  |  |
| KEEP | `stormpy.simulator.Simulator` | class | `stormpy.simulator` | Python |  |  |
| KEEP | `stormpy.simulator.SimulatorActionMode` | enum | `stormpy.simulator` | Python |  |  |
| KEEP | `stormpy.simulator.SimulatorObservationMode` | enum | `stormpy.simulator` | Python |  |  |
| KEEP | `stormpy.simulator.SparseSimulator` | class | `stormpy.simulator` | Python |  |  |
| PRIVATE | `stormpy.simulator.stormpy` | module | `stormpy` | Python |  | Imported implementation/helper module; do not expose as API. |

## `stormpy.dft` (optional: DFT)

48 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.dft.analyze_dft` | function | `stormpy.dft` | Python |  |  |
| KEEP | `stormpy.dft.ApproximationHeuristic` | enum | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.build_model` | function | `stormpy.dft` | Python |  |  |
| KEEP | `stormpy.dft.compute_dependency_conflicts` | function | `stormpy.dft` | Python |  |  |
| KEEP | `stormpy.dft.compute_relevant_events` | function | `stormpy.dft._dft` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.dft.DFT_double` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.DFT | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.DFT_ratfunc` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.DFT | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.DFTBE_double` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.DFTBE | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.DFTBE_ratfunc` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.DFTBE | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.DFTDependency_double` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.DFTDependency | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.DFTDependency_ratfunc` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.DFTDependency | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.DFTElement_double` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.DFTElement | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.DFTElement_ratfunc` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.DFTElement | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.dft.DFTElementType` | enum | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.DftIndependentModule` | class | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.DFTInstantiator` | class | `stormpy.dft._dft` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.dft.DFTSimulator_double` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.DFTSimulator | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.DFTSimulator_ratfunc` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.DFTSimulator | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.DFTState_double` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.DFTState | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.DFTState_ratfunc` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.DFTState | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.dft.DFTStateInfo` | class | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.DftSymmetries` | class | `stormpy.dft._dft` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.dft.ExplicitDFTModelBuilder_double` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.ExplicitDFTModelBuilder | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.ExplicitDFTModelBuilder_ratfunc` | class | `stormpy.dft._dft` | C++ binding | stormpy.dft.ExplicitDFTModelBuilder | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.dft.export_dft_json_file` | function | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.export_dft_json_string` | function | `stormpy.dft._dft` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.dft.export_parametric_dft_json_file` | function | `stormpy.dft._dft` | C++ binding | stormpy.dft.export_dft_json_file | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.export_parametric_dft_json_string` | function | `stormpy.dft._dft` | C++ binding | stormpy.dft.export_dft_json_string | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.dft.FailableElement` | class | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.FailableElements` | class | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.FailableIterator` | class | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.get_parameters` | function | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.has_potential_modeling_issues` | function | `stormpy.dft` | Python |  |  |
| KEEP | `stormpy.dft.is_well_formed` | function | `stormpy.dft` | Python |  |  |
| KEEP | `stormpy.dft.load_dft_galileo_file` | function | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.load_dft_json_file` | function | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.load_dft_json_string` | function | `stormpy.dft._dft` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.dft.load_parametric_dft_galileo_file` | function | `stormpy.dft._dft` | C++ binding | stormpy.dft.load_dft_galileo_file | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.load_parametric_dft_json_file` | function | `stormpy.dft._dft` | C++ binding | stormpy.dft.load_dft_json_file | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.dft.load_parametric_dft_json_string` | function | `stormpy.dft._dft` | C++ binding | stormpy.dft.load_dft_json_string | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.dft.modules` | module | `stormpy.dft.modules` | Python |  |  |
| KEEP | `stormpy.dft.modules_json` | function | `stormpy.dft.modules` | Python |  |  |
| KEEP | `stormpy.dft.prepare_for_analysis` | function | `stormpy.dft` | Python |  |  |
| KEEP | `stormpy.dft.RandomGenerator` | class | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.RelevantEvents` | class | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.SimulationStepResult` | enum | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.SimulationTraceResult` | enum | `stormpy.dft._dft` | C++ binding |  |  |
| KEEP | `stormpy.dft.transform_dft` | function | `stormpy.dft` | Python |  |  |

## `stormpy.dft.modules` (optional: DFT)

2 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.dft.modules.modules_json` | function | `stormpy.dft.modules` | Python |  |  |
| PRIVATE | `stormpy.dft.modules.stormpy` | module | `stormpy` | Python |  | Imported implementation/helper module; do not expose as API. |

## `stormpy.dft.simulator` (optional: DFT)

2 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.dft.simulator.DftSimulator` | class | `stormpy.dft.simulator` | Python |  |  |
| PRIVATE | `stormpy.dft.simulator.stormpy` | module | `stormpy` | Python |  | Imported implementation/helper module; do not expose as API. |

## `stormpy.gspn` (optional: GSPN)

10 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.gspn.GSPN` | class | `stormpy.gspn._gspn` | C++ binding |  |  |
| KEEP | `stormpy.gspn.GSPNBuilder` | class | `stormpy.gspn._gspn` | C++ binding |  |  |
| KEEP | `stormpy.gspn.GSPNParser` | class | `stormpy.gspn._gspn` | C++ binding |  |  |
| KEEP | `stormpy.gspn.GSPNToJaniBuilder` | class | `stormpy.gspn._gspn` | C++ binding |  |  |
| KEEP | `stormpy.gspn.ImmediateTransition` | class | `stormpy.gspn._gspn` | C++ binding |  |  |
| KEEP | `stormpy.gspn.LayoutInfo` | class | `stormpy.gspn._gspn` | C++ binding |  |  |
| KEEP | `stormpy.gspn.Place` | class | `stormpy.gspn._gspn` | C++ binding |  |  |
| KEEP | `stormpy.gspn.TimedTransition` | class | `stormpy.gspn._gspn` | C++ binding |  |  |
| KEEP | `stormpy.gspn.Transition` | class | `stormpy.gspn._gspn` | C++ binding |  |  |
| KEEP | `stormpy.gspn.TransitionPartition` | class | `stormpy.gspn._gspn` | C++ binding |  |  |

## `stormpy.pars` (optional: PARS)

27 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.pars.create_region_checker` | function | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.create_region_refinement_checker` | function | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.DtmcParameterLiftingModelChecker` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.gather_derivatives` | function | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.MdpParameterLiftingModelChecker` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.ModelInstantiator` | class | `stormpy.pars` | Python |  |  |
| KEEP | `stormpy.pars.ModelType` | enum | `stormpy.storage._storage` | C++ binding |  |  |
| KEEP | `stormpy.pars.ParameterRegion` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.PartialPCtmcInstantiator` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.PartialPDtmcInstantiator` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.PartialPMaInstantiator` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.PartialPMdpInstantiator` | class | `stormpy.pars._pars` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.pars.PCtmcExactInstantiationChecker` | class | `stormpy.pars._pars` | C++ binding | stormpy.pars.PCtmcInstantiationChecker | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.pars.PCtmcInstantiationChecker` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.PCtmcInstantiator` | class | `stormpy.pars._pars` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.pars.PDtmcExactInstantiationChecker` | class | `stormpy.pars._pars` | C++ binding | stormpy.pars.PDtmcInstantiationChecker | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.pars.PDtmcInstantiationChecker` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.PDtmcInstantiator` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.PMaInstantiator` | class | `stormpy.pars._pars` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.pars.PMdpExactInstantiationChecker` | class | `stormpy.pars._pars` | C++ binding | stormpy.pars.PMdpInstantiationChecker | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.pars.PMdpInstantiationChecker` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.PMdpInstantiator` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.RegionModelChecker` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.RegionRefinementChecker` | class | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.RegionResult` | enum | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.RegionResultHypothesis` | enum | `stormpy.pars._pars` | C++ binding |  |  |
| KEEP | `stormpy.pars.simplify_model` | function | `stormpy.pars` | Python |  |  |

## `stormpy.pomdp` (optional: POMDP)

41 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.pomdp.apply_unknown_fsc` | function | `stormpy.pomdp` | Python |  |  |
| CONSOLIDATE | `stormpy.pomdp.BeliefExplorationModelCheckerDouble` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.BeliefExplorationModelChecker | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.BeliefExplorationModelCheckerOptionsDouble` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.BeliefExplorationModelCheckerOptions | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.BeliefExplorationPomdpModelCheckerResultDouble` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.BeliefExplorationPomdpModelCheckerResult | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.BeliefMdpExplorerDouble` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.BeliefMdpExplorer | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.BeliefSupportTrackerDouble` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.BeliefSupportTracker | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.BeliefSupportTrackerExact` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.BeliefSupportTracker | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.pomdp.BeliefSupportWinningRegion` | class | `stormpy.pomdp._pomdp` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.pomdp.BeliefSupportWinningRegionQueryInterfaceDouble` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.BeliefSupportWinningRegionQueryInterface | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.pomdp.create_interactive_mc` | function | `stormpy.pomdp._pomdp` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.pomdp.create_iterative_qualitative_search_solver_Double` | function | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.create_iterative_qualitative_search_solver | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.pomdp.create_nondeterminstic_belief_tracker` | function | `stormpy.pomdp` | Python |  |  |
| KEEP | `stormpy.pomdp.create_observation_trace_unfolder` | function | `stormpy.pomdp` | Python |  |  |
| CONSOLIDATE | `stormpy.pomdp.GenerateMonitorVerifierDouble` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.GenerateMonitorVerifier | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.GenerateMonitorVerifierDoubleOptions` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.GenerateMonitorVerifierOptions | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.GenerateMonitorVerifierExact` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.GenerateMonitorVerifier | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.GenerateMonitorVerifierExactOptions` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.GenerateMonitorVerifierOptions | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.pomdp.IterativeQualitativeSearchOptions` | class | `stormpy.pomdp._pomdp` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.pomdp.IterativeQualitativeSearchSolverDouble` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.IterativeQualitativeSearchSolver | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.pomdp.make_canonic` | function | `stormpy.pomdp` | Python |  |  |
| KEEP | `stormpy.pomdp.make_simple` | function | `stormpy.pomdp` | Python |  |  |
| CONSOLIDATE | `stormpy.pomdp.MonitorVerifierDouble` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.MonitorVerifier | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.MonitorVerifierExact` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.MonitorVerifier | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.NondeterministicBeliefTrackerDoubleSparse` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.NondeterministicBeliefTrackerSparse | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.NondeterministicBeliefTrackerDoubleSparseOptions` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.NondeterministicBeliefTrackerSparseOptions | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.NondeterministicBeliefTrackerExactSparse` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.NondeterministicBeliefTrackerSparse | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.NondeterministicBeliefTrackerExactSparseOptions` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.NondeterministicBeliefTrackerSparseOptions | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.ObservationTraceUnfolderDouble` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.ObservationTraceUnfolder | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.ObservationTraceUnfolderExact` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.ObservationTraceUnfolder | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.ObservationTraceUnfolderInterval` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.ObservationTraceUnfolder | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.pomdp.ObservationTraceUnfolderOptions` | class | `stormpy.pomdp._pomdp` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.pomdp.ObservationTraceUnfolderParametric` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.ObservationTraceUnfolder | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.ObservationTraceUnfolderRationalInterval` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.ObservationTraceUnfolder | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.pomdp.PomdpFscApplicationMode` | enum | `stormpy.pomdp._pomdp` | C++ binding |  |  |
| KEEP | `stormpy.pomdp.PomdpMemory` | class | `stormpy.pomdp._pomdp` | C++ binding |  |  |
| KEEP | `stormpy.pomdp.PomdpMemoryBuilder` | class | `stormpy.pomdp._pomdp` | C++ binding |  |  |
| KEEP | `stormpy.pomdp.PomdpMemoryPattern` | enum | `stormpy.pomdp._pomdp` | C++ binding |  |  |
| CONSOLIDATE | `stormpy.pomdp.prepare_pomdp_for_qualitative_search_Double` | function | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.prepare_pomdp_for_qualitative_search | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.SparseBeliefStateDouble` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.SparseBeliefState | Value-type specialization; expose one Python dispatcher or facade. |
| CONSOLIDATE | `stormpy.pomdp.SparseBeliefStateExact` | class | `stormpy.pomdp._pomdp` | C++ binding | stormpy.pomdp.SparseBeliefState | Value-type specialization; expose one Python dispatcher or facade. |
| KEEP | `stormpy.pomdp.unfold_memory` | function | `stormpy.pomdp` | Python |  |  |

## `stormpy.info`

9 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.info.storm_build_type` | function | `stormpy.info` | Python |  |  |
| KEEP | `stormpy.info.storm_development_version` | function | `stormpy.info` | Python |  |  |
| KEEP | `stormpy.info.storm_directory` | function | `stormpy.info` | Python |  |  |
| KEEP | `stormpy.info.storm_exact_use_cln` | function | `stormpy.info` | Python |  |  |
| KEEP | `stormpy.info.storm_from_system` | function | `stormpy.info` | Python |  |  |
| KEEP | `stormpy.info.storm_origin_info` | function | `stormpy.info` | Python |  |  |
| KEEP | `stormpy.info.storm_ratfunc_use_cln` | function | `stormpy.info` | Python |  |  |
| KEEP | `stormpy.info.storm_version` | function | `stormpy.info` | Python |  |  |
| KEEP | `stormpy.info.Version` | class | `stormpy.info._info` | C++ binding |  |  |

## `stormpy.exceptions`

2 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| PRIVATE | `stormpy.exceptions.storm_error` | module | `stormpy.exceptions.storm_error` | Python |  | Imported implementation/helper module; do not expose as API. |
| KEEP | `stormpy.exceptions.StormError` | class | `stormpy.exceptions.storm_error` | Python |  |  |

## `stormpy.examples`

0 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|

## `stormpy.examples.files`

24 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.examples.files.dft_galileo_hecs` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.dft_json_and` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.drn_ctmc_dft` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.drn_pdtmc_die` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.drn_pomdp_maze` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.gspn_pnml_simple` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.gspn_pnpro_simple` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.jani_dtmc_die` | constant | `builtins` | external |  |  |
| PRIVATE | `stormpy.examples.files.os` | module | `os` | external |  | Imported implementation/helper module; do not expose as API. |
| KEEP | `stormpy.examples.files.prism_dtmc_brp` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_dtmc_die` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_ma_simple` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_mdp_coin_2_2` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_mdp_firewire` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_mdp_maze` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_mdp_maze_multigoal` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_mdp_slipgrid` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_mdp_slipgrid_sketch` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_par_pomdp_maze` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_pdtmc_brp` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_pdtmc_die` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_pmdp_coin_two_dice` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.prism_pomdp_maze` | constant | `builtins` | external |  |  |
| KEEP | `stormpy.examples.files.testfile_dir` | constant | `builtins` | external |  |  |

## `stormpy.pycarl`

24 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.pycarl.abs` | function | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.BoundType` | enum | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.carl_version` | function | `stormpy.pycarl` | Python |  |  |
| KEEP | `stormpy.pycarl.ceil` | function | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.clear_monomial_pool` | function | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.clear_pools` | function | `stormpy.pycarl` | Python |  |  |
| KEEP | `stormpy.pycarl.clear_variable_pool` | function | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.cln` | module | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.create_monomial` | function | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.div` | function | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.floor` | function | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.gmp` | module | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.has_cln` | function | `stormpy.pycarl` | Python |  |  |
| KEEP | `stormpy.pycarl.inf` | constant | `stormpy.pycarl.infinity` | Python |  |  |
| KEEP | `stormpy.pycarl.infinity` | module | `stormpy.pycarl.infinity` | Python |  |  |
| KEEP | `stormpy.pycarl.Interval` | class | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.isInteger` | function | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.Monomial` | class | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.NoPicklingSupport` | class | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.pow` | function | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.quotient` | function | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.Variable` | class | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.variable_with_name` | function | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |
| KEEP | `stormpy.pycarl.VariableType` | enum | `stormpy.pycarl._pycarl_core` | C++ binding |  |  |

## `stormpy.pycarl.formula`

2 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.pycarl.formula.FormulaType` | enum | `stormpy.pycarl.formula` | Python |  |  |
| KEEP | `stormpy.pycarl.formula.Relation` | enum | `stormpy.pycarl.formula` | Python |  |  |

## `stormpy.pycarl.cln`

21 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.pycarl.cln.abs` | function | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.ceil` | function | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.create_factorized_polynomial` | function | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.denominator` | function | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.div` | function | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.expand` | function | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.Factorization` | class | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.factorization_cache` | constant | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.FactorizedPolynomial` | class | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.FactorizedRationalFunction` | class | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.floor` | function | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.Integer` | class | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.Interval` | class | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.isInteger` | function | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.numerator` | function | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.Polynomial` | class | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.pow` | function | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.quotient` | function | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.Rational` | class | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.RationalFunction` | class | `stormpy.pycarl.cln` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.Term` | class | `stormpy.pycarl.cln` | Python |  |  |

## `stormpy.pycarl.cln.formula`

4 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.pycarl.cln.formula.Constraint` | class | `stormpy.pycarl.formula` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.formula.Formula` | class | `stormpy.pycarl.formula` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.formula.SimpleConstraint` | class | `stormpy.pycarl.formula` | Python |  |  |
| KEEP | `stormpy.pycarl.cln.formula.SimpleConstraintRatFunc` | class | `stormpy.pycarl.formula` | Python |  |  |

## `stormpy.pycarl.gmp`

21 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.pycarl.gmp.abs` | function | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.ceil` | function | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.create_factorized_polynomial` | function | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.denominator` | function | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.div` | function | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.expand` | function | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.Factorization` | class | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.factorization_cache` | constant | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.FactorizedPolynomial` | class | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.FactorizedRationalFunction` | class | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.floor` | function | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.Integer` | class | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.Interval` | class | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.isInteger` | function | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.numerator` | function | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.Polynomial` | class | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.pow` | function | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.quotient` | function | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.Rational` | class | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.RationalFunction` | class | `stormpy.pycarl.gmp` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.Term` | class | `stormpy.pycarl.gmp` | Python |  |  |

## `stormpy.pycarl.gmp.formula`

4 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.pycarl.gmp.formula.Constraint` | class | `stormpy.pycarl.formula` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.formula.Formula` | class | `stormpy.pycarl.formula` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.formula.SimpleConstraint` | class | `stormpy.pycarl.formula` | Python |  |  |
| KEEP | `stormpy.pycarl.gmp.formula.SimpleConstraintRatFunc` | class | `stormpy.pycarl.formula` | Python |  |  |

## `stormpy.pycarl.convert`

5 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| PRIVATE | `stormpy.pycarl.convert.cln_converter` | module | `stormpy.pycarl.convert.cln_converter` | Python |  | Imported implementation/helper module; do not expose as API. |
| KEEP | `stormpy.pycarl.convert.convert_to_cln` | function | `stormpy.pycarl.convert` | Python |  |  |
| KEEP | `stormpy.pycarl.convert.convert_to_gmp` | function | `stormpy.pycarl.convert` | Python |  |  |
| PRIVATE | `stormpy.pycarl.convert.gmp_converter` | module | `stormpy.pycarl.convert.gmp_converter` | Python |  | Imported implementation/helper module; do not expose as API. |
| KEEP | `stormpy.pycarl.convert.has_cln` | constant | `builtins` | external |  |  |

## `stormpy.pycarl.parse`

2 entries.

| Decision | Public import path | Kind | Defined by | Layer | Target / group | Notes |
|---|---|---|---|---|---|---|
| KEEP | `stormpy.pycarl.parse.deserialize` | function | `stormpy.pycarl.parse` | Python |  |  |
| KEEP | `stormpy.pycarl.parse.ParserError` | class | `stormpy.pycarl.parse` | Python |  |  |
