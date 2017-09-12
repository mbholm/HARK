'''
Specifies examples of the full set of parameters required to solve various
consumption-saving models.  These models can be found in ConsIndShockModel,
ConsAggShockModel, ConsPrefShockModel, and ConsMarkovModel.
'''
from copy import copy
import numpy as np

# -----------------------------------------------------------------------------
# --- Define all of the parameters for the perfect foresight model ------------
# -----------------------------------------------------------------------------

CRRA = 2.0                          # Coefficient of relative risk aversion
Rfree = 1.03                        # Interest factor on assets
DiscFac = 1/1.01                      # Intertemporal discount factor
LivPrb = [1]                     # Survival probability
PermGroFac = [1.00]                 # Permanent income growth factor
AgentCount = 10000                  # Number of agents of this type (only matters for simulation)
aNrmInitMean = 0.0                  # Mean of log initial assets (only matters for simulation)
aNrmInitStd  = 1.0                  # Standard deviation of log initial assets (only for simulation)
pLvlInitMean = 0.0                  # Mean of log initial permanent income (only matters for simulation)
pLvlInitStd  = 0.0                  # Standard deviation of log initial permanent income (only matters for simulation)
PermGroFacAgg = 1.0                 # Aggregate permanent income growth factor (only matters for simulation)
T_age = None                        # Age after which simulated agents are automatically killed
T_cycle = 1                         # Number of periods in the cycle for this agent type

# Make a dictionary to specify a perfect foresight consumer type
init_perfect_foresight = { 'CRRA': CRRA,
                           'Rfree': Rfree,
                           'DiscFac': DiscFac,
                           'LivPrb': LivPrb,
                           'PermGroFac': PermGroFac,
                           'AgentCount': AgentCount,
                           'aNrmInitMean' : aNrmInitMean,
                           'aNrmInitStd' : aNrmInitStd,
                           'pLvlInitMean' : pLvlInitMean,
                           'pLvlInitStd' : pLvlInitStd,
                           'PermGroFacAgg' : PermGroFacAgg,
                           'T_age' : T_age,
                           'T_cycle' : T_cycle
                          }
                                                   
# -----------------------------------------------------------------------------
# --- Define additional parameters for the idiosyncratic shocks model ---------
# -----------------------------------------------------------------------------

# Parameters for constructing the "assets above minimum" grid
aXtraMin = 0.001                    # Minimum end-of-period "assets above minimum" value
aXtraMax = 20                       # Maximum end-of-period "assets above minimum" value               
aXtraExtra = None                   # Some other value of "assets above minimum" to add to the grid, not used
aXtraNestFac = 3                    # Exponential nesting factor when constructing "assets above minimum" grid
aXtraCount = 48                     # Number of points in the grid of "assets above minimum"

# Parameters describing the income process
PermShkCount = 7                    # Number of points in discrete approximation to permanent income shocks
TranShkCount = 7                    # Number of points in discrete approximation to transitory income shocks
PermShkStd = [0.05]                  # Standard deviation of log permanent income shocks
TranShkStd = [0.5]                  # Standard deviation of log transitory income shocks
UnempPrb = 0.05                     # Probability of unemployment while working
UnempPrbRet = 0.005                 # Probability of "unemployment" while retired
IncUnemp = 0.25                      # Unemployment benefits replacement rate
IncUnempRet = 0.0                   # "Unemployment" benefits when retired
tax_rate = 0.0                      # Flat income tax rate
T_retire = 0                        # Period of retirement (0 --> no retirement)

# A few other parameters
BoroCnstArt = 0.0                  # Artificial borrowing constraint; imposed minimum level of end-of period assets
CubicBool = False                  # Use cubic spline interpolation when True, linear interpolation when False
vFuncBool = True                   # Whether to calculate the value function during solution

# Make a dictionary to specify an idiosyncratic income shocks consumer
init_idiosyncratic_shocks = { 'CRRA': CRRA,
                              'Rfree': Rfree,
                              'DiscFac': DiscFac,
                              'LivPrb': LivPrb,
                              'PermGroFac': PermGroFac,
                              'AgentCount': AgentCount,
                              'aXtraMin': aXtraMin,
                              'aXtraMax': aXtraMax,
                              'aXtraNestFac':aXtraNestFac,
                              'aXtraCount': aXtraCount,
                              'aXtraExtra': [aXtraExtra],
                              'PermShkStd': PermShkStd,
                              'PermShkCount': PermShkCount,
                              'TranShkStd': TranShkStd,
                              'TranShkCount': TranShkCount,
                              'UnempPrb': UnempPrb,
                              'UnempPrbRet': UnempPrbRet,
                              'IncUnemp': IncUnemp,
                              'IncUnempRet': IncUnempRet,
                              'BoroCnstArt': BoroCnstArt,
                              'tax_rate':0.0,
                              'vFuncBool':vFuncBool,
                              'CubicBool':CubicBool,
                              'T_retire':T_retire,
                              'aNrmInitMean' : aNrmInitMean,
                              'aNrmInitStd' : aNrmInitStd,
                              'pLvlInitMean' : pLvlInitMean,
                              'pLvlInitStd' : pLvlInitStd,
                              'PermGroFacAgg' : PermGroFacAgg,
                              'T_age' : T_age,
                              'T_cycle' : T_cycle
                             }
                             
# Make a dictionary to specify a lifecycle consumer with a finite horizon
init_lifecycle = copy(init_idiosyncratic_shocks)
init_lifecycle['PermGroFac'] = [1,1,1,1,1,1,1,1,1,1]
init_lifecycle['PermShkStd'] = [0,0,0,0,0,0,0,0,0,0]
init_lifecycle['TranShkStd'] = [0,0,0,0,0,0,0,0,0,0]
init_lifecycle['LivPrb']     = [1,1,1,1,1,1,1,1,1,1]
init_lifecycle['IncUnemp']   = 1
init_lifecycle['T_cycle']    = 10
init_lifecycle['T_retire']   = None
init_lifecycle['T_age']      = 11 # Make sure that old people die at terminal age and don't turn into newborns!


