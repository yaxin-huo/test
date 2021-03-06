### This file is a part of the Syncpy library.
### Copyright 2015, ISIR / Universite Pierre et Marie Curie (UPMC)
### Main contributor(s): Giovanna Varni, Marie Avril,
### syncpy@isir.upmc.fr
### 
### This software is a computer program whose for investigating
### synchrony in a fast and exhaustive way. 
### 
### This software is governed by the CeCILL-B license under French law
### and abiding by the rules of distribution of free software.  You
### can use, modify and/ or redistribute the software under the terms
### of the CeCILL-B license as circulated by CEA, CNRS and INRIA at the
### following URL "http://www.cecill.info".

### As a counterpart to the access to the source code and rights to
### copy, modify and redistribute granted by the license, users are
### provided only with a limited warranty and the software's author,
### the holder of the economic rights, and the successive licensors
### have only limited liability.
### 
### In this respect, the user's attention is drawn to the risks
### associated with loading, using, modifying and/or developing or
### reproducing the software by the user in light of its specific
### status of free software, that may mean that it is complicated to
### manipulate, and that also therefore means that it is reserved for
### developers and experienced professionals having in-depth computer
### knowledge. Users are therefore encouraged to load and test the
### software's suitability as regards their requirements in conditions
### enabling the security of their systems and/or data to be ensured
### and, more generally, to use and operate it in the same conditions
### as regards security.
### 
### The fact that you are presently reading this means that you have
### had knowledge of the CeCILL-B license and that you accept its terms.

"""
.. moduleauthor:: Adem Usta and Giovanna Varni
"""
import sys  # To be able to import from parent directory
import numpy as np  # For math operation
import pandas as pd  # For DataFrame
from scipy import stats  # For computing p-value
import matplotlib.pyplot as plt  # Plotting package
import networkx as nx
from statsmodels.regression.linear_model import \
    OLS  # Class to compute autoregressive model with 'Ordinary Least Squares'  method
from statsmodels.tsa.tsatools import lagmat2ds  # Specific function
from statsmodels.tools.tools import add_constant  # Specific function

sys.path.insert(0, '../../../../')
import DataFrom2Persons.Univariate.Continuous.Linear.GrangerCausality as GC  # For Pairwise Granger Causality


class ConditionalGrangerCausality:
    """
	It computes Conditional Granger Causality among signals. It assesses whether the interaction between two signals is direct
	or is mediated by other signals and wheter the causal influence is due to differential time delays in the driving inputs.
	The algorithm computes bi-directional pairwise Granger causality test between all the signals, to detect temporary direct links.
	For each detected link, a conditional test is made to know if the link between the two signals is mediated by the other signals.
	At the end of the test, a graph is shown to see the true links among the signals.

	**Reference :**

	* Xiaotong Wen, Govindan Rangarajan, and Mingzhou Ding. Multivariate Granger causality : an estimation framework based on factorization of the spectral density matrix. Philosophical Transactions of the Royal Society of London A : Mathematical, Physical and Engineering Sciences, 371(1997) :20110610, August 2013.

	:param max_lag:
		The number of maximum lag (in samples) with which the autoregressive model will be computed.
		It ranges in [1;length(x)]. Default :1.
	:type max_lag: int

	:param criterion: A string that contains the name of the selected criterion to estimate optimal number of lags value.
		Two choices are possible :
			1. 'bic' (Bayesian Information Criterion);
			2. 'aic' (Akaike information criterion)
		Default : 'bic'
	:type criterion: str

	:param plot:
		if True the plot of correlation function is returned. Default: False
	:type plot: bool
	"""

    ''' Constructor '''

    def __init__(self, max_lag=1, criterion='bic', plot=False):
        ' Raise error if parameters are not in the correct type '
        if not (isinstance(criterion, str)): raise TypeError("Requires criterion to be a str")
        if not (isinstance(max_lag, int)): raise TypeError("Requires max_lag to be an int")
        if not (isinstance(plot, bool)): raise TypeError("Requires plot to be a bool")

        ' Raise error if parameters do not respect input rules '
        if max_lag <= 0: raise ValueError("Requires max_lag to be a strictly positive scalar")
        if criterion != 'bic' and criterion != 'aic': raise ValueError("Requires criterion to be 'bic' or 'aic'")

        ' Attributes to initialise when creating the object '
        self._max_lag = max_lag
        self._criterion = criterion
        self._plot = plot

    def plot_result(self, result):
        """
		It plots the final result of the module : a graphic that shows the links between the signals.

		:param result:
			Conditional Granger Causality result from compute()
		:type result: dict

		:returns: plt.figure
			-- A figure that contains the nodes graph
		"""

        ' Raise error if parameters are not in the correct type '
        if not (isinstance(result, dict)): raise TypeError("Requires result to be a dictionary")

        ' Raise error if not the good dictionary '
        if not 'link_matrix' in result: raise ValueError("Requires dictionary to be the output of compute() method")

        # Define a plot figure
        fig = plt.figure()
        ax1 = fig.add_subplot(111)

        # Option on axis
        ax1.set_title('Causality graphic')
        plt.axis('off')

        # Creating a new graph
        G = nx.DiGraph()
        N = np.shape(result['link_matrix'])[0]

        for k in range(0, N):
            G.add_node(str(k + 1))

        for i in range(0, N):
            for j in range(0, N):
                if result['link_matrix'][i, j] == 1:
                    G.add_edge(str(j + 1), str(i + 1))

        # Plot graphic :
        nx.draw_networkx(G, pos=nx.spring_layout(G), with_label=True, node_size=600, node_color='white',
                         edge_color='black')
        self._G = G

        # Return figure
        return fig

    ''' Computes ConditionalGrangerCausality test '''

    def compute(self, *signals):
        """
		This method computes the ConditionalGrangerCausality. At the end of the computation, a graph is made to show the links between the signals.

		:param signals:
			list of signals, one per person.
		:type signals: list[pd.DataFrame]

		:returns: dict
			-- matrix of links between the signals.

		"""

        ' Raise error if parameters are not in the correct type '
        for i in range(0, len(signals)):
            if not (isinstance(signals[i], pd.DataFrame)): raise TypeError(
                "Requires signal " + str(i + 1) + " to be a pd.DataFrame, ")

        ' Raise error if DataFrames have not the same size '

        for i in range(0, len(signals)):
            if len(signals[0]) != len(signals[i]): raise ValueError(
                "All the signals must have the same size. Signal " + str(
                    i + 1) + " does not have the same size as signal 1")

        # Saving the size of signals (they all supposed to have the same size)
        T = len(signals[0])

        # Converting DataFrames to arrays :
        SIGNALS = np.zeros((T, len(signals)))

        for i in range(0, len(signals)):
            SIGNALS[:, i] = np.array(signals[i]).reshape(T)

        # Creating Matrix to save the links between the signals :
        M_direct = np.zeros((len(signals), len(signals)))

        # Testing for direct links between signals :
        print "Results of pairwise analysis:\n"
        for i in range(0, len(signals)):
            for j in range(0, len(signals)):
                if (i != j):
                    gc = GC.GrangerCausality(max_lag=self._max_lag, criterion=self._criterion, plot=False)
                    gc_res = gc.compute(signals[i], signals[j])
                    if gc_res['ratio'] > 0 and gc_res['p_value'] < 0.01:
                        print "signal", j + 1, "->", i + 1, "detected"
                        M_direct[i, j] = 1

        # Computing the FULL VAR model :

        # First we have to determine the optimal order according to the given criterion
        olag_AR = np.zeros((len(signals), 1))

        # For each order, computing VAR :
        for k in range(0, len(signals)):

            # Permuting columns to compute VAR :
            SIGNALS_V = np.concatenate((SIGNALS[:, k:], SIGNALS[:, 0:k]), axis=1)

            criterion_value = np.zeros((self._max_lag, 1))

            # Testing each order :
            for lag in range(1, self._max_lag + 1):

                data = lagmat2ds(SIGNALS_V, lag, trim='both', dropex=1)
                datajoint = add_constant(data[:, 1:], prepend=False)
                OLS_ = OLS(data[:, 0], datajoint).fit()

                # Saving AIC or BIC temporary values :
                if self._criterion == 'bic':
                    criterion_value[lag - 1] = OLS_.bic
                elif self._criterion == 'aic':
                    criterion_value[lag - 1] = OLS_.aic

            olag_AR[k] = criterion_value.argmin() + 1

        # The optimal order is chosen as the mean order between all the estimated orders from all models
        olag = int(np.ceil(np.mean(olag_AR)))

        # Now we can compute the VAR model with the computed order :
        VAR_resid = np.zeros((T - olag, len(signals)))

        for k in range(0, len(signals)):
            # Permuting columns to compute VAR :
            SIGNALS_P = np.concatenate((SIGNALS[:, k:], SIGNALS[:, 0:k]), axis=1)

            data = lagmat2ds(SIGNALS_P, olag, trim='both', dropex=1)
            datajoint = add_constant(data[:, 1:], prepend=False)
            OLS_ = OLS(data[:, 0], datajoint).fit()
            VAR_resid[:, k] = OLS_.resid

        # Computing the noise covariance matrix of the full model :
        VAR_noise_matrix = np.cov(VAR_resid.T)

        M_final = np.zeros((len(signals), len(signals)))

        # Testing for mediated links between signals :
        print "\n"
        for i in range(0, len(signals)):
            for j in range(0, len(signals)):
                if M_direct[i, j] == 1:
                    # We have detected a "direct link", we need to test with other signals to know if there is a mediated link:
                    for k in range(0, len(signals)):
                        if (k != j) and (k != i):
                            SIGNALS_M = np.delete(SIGNALS, [i, j], 1)
                            S = np.concatenate((SIGNALS[:, i].reshape(T, 1), SIGNALS_M[:, 0:].reshape(T, 2)), axis=1)
                            data = lagmat2ds(S, olag, trim='both', dropex=1)
                            datajoint = add_constant(data[:, 1:], prepend=False)
                            OLS_ = OLS(data[:, 0], datajoint).fit()
                            var_noise = np.var(OLS_.resid)
                            ratio = np.log(var_noise) - np.log(VAR_noise_matrix[i, i])
                            if ratio < 0.01:
                                print "signal", j + 1, "->", i + 1, " is mediated by signal", k + 1
                                M_direct[i, j] = 0
                                M_final[i, k] = 1
                                M_final[k, j] = 1
                                break
                            else:
                                M_final[i, j] = 1

        results = dict()
        results['link_matrix'] = M_final

        if (self._plot == True):
            plt.ion()
            self.plot_result(results)

        return results
