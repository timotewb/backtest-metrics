def sharpe_ratio(returns, days, rf=0):
       
    import numpy as np
    
    sr = np.sqrt(days) * ( (np.nanmean(returns) - rf) / np.nanstd(returns) )

    #--- if value is +-inf then set to Nan
    if sr == np.inf or sr == -np.inf:
        sr = np.nan

    return sr
