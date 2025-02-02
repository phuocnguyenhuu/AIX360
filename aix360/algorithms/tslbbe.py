import abc
import numpy as np

from aix360.algorithms.lbbe import LocalBBExplainer
from aix360.algorithms.tsutils.tsframe import tsFrame


class TSLocalBBExplainer(LocalBBExplainer):
    """Base class for local black box explainers for univariate time series forecasting.
    This class extends :py:mod:``LocalBBExplainer`` for univariate time series forecasting.
    Such explainers generally are model agnostic and would require forecaster's predict function."""

    def __init__(self, *argv, **kwargs):
        super(TSLocalBBExplainer, self).__init__(*argv, **kwargs)

    @abc.abstractmethod
    def _explain_instance(
        self, ts: tsFrame, ts_related: tsFrame = None, **explain_params
    ):
        raise NotImplementedError("This method is not implemented.")

    def explain_instance(
        self, ts: tsFrame, ts_related: tsFrame = None, **explain_params
    ):
        """Explain the forecast made by the forecaster at a certain point in time
        (**local explanation**).

        Args
            ts (tsFrame): The future univariate time series ``tsFrame`` to use for forecasting that
                extends forward from the end of training ``tsFrame`` (``ts_train``) or
                ``timestamp_start`` for the requested number of periods.
                This can be generated using :py:mod:`aix360.algorithms.tsframe.tsFrame`.
                A ``tsFrame`` is a pandas ``DataFrame`` indexed by ``Timestamp`` objects
                (that is ``DatetimeIndex``). Each column corresponds to a target to forecast.
            ts_related (tsFrame, optional): The related time series ``tsFrame`` containing
                the external regressors. A ``tsFrame`` is a pandas ``DataFrame`` indexed by
                ``Timestamp`` objects (that is ``DatetimeIndex``). Each column corresponds to a
                related external regressor. Defaults to None.
            explain_params: Arbitrary explainer parameters.

        Returns:
            explanation : Union[List[Dict], Dict]
                Returns a dict with explanation object or a list of multiple explanations
                if the forecast horizon is greater than one, where each element corresponds
                to the local explanation for that particular time step in the forecast horizon.
        """

        return self._explain_instance(ts=ts, ts_related=ts_related, **explain_params)
