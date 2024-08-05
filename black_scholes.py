import numpy as np
import scipy.stats as stats

class BS: 
    def __init__(self, spot, strike, rate, days, volatility, multiplier=100): 
        self.spot = spot
        self.strike = strike
        self.rate = rate
        self.days = days / 365
        self.volatility = volatility
        self.multiplier = multiplier

        self.d1 = (np.log(self.spot/self.strike) + \
                   (self.rate+0.5*self.volatility**2)*(self.days)) \
                   / (self.volatility * np.sqrt(self.days))
        self.d2 = self.d1 - self.volatility*np.sqrt(self.days)

        self.N_tag_d1 = (np.exp(-0.5*self.d1**2)) / (np.sqrt(2*np.pi))
    

    def call_price(self): 
        a = self.spot*stats.norm.cdf(self.d1)
        b = np.exp(-self.rate*self.days)*self.strike*stats.norm.cdf(self.d2)
        return '{:,.0f}'.format(round((a-b)*self.multiplier, 0))
    
    def put_price(self):
        a = self.strike*np.exp(-self.rate*self.days)*stats.norm.cdf(-self.d2)
        b = self.spot*stats.norm.cdf(-self.d1)
        return '{:,.0f}'.format(round((a-b)*self.multiplier, 0))
    
    def call_delta(self): 
        return round(stats.norm.cdf(self.d1), 4)
    
    def put_delta(self): 
        return round(stats.norm.cdf(self.d1) - 1, 4)
    
    def call_gamma(self):
        return round(self.N_tag_d1 / (self.spot * self.volatility * np.sqrt(self.days)), 4)
    
    def put_gamma(self): 
        return round(self.call_gamma(), 4)
    
    def call_vega(self): 
        return round(self.spot * np.sqrt(self.days) * self.N_tag_d1 / 100, 4)
    
    def put_vega(self): 
        return round(self.call_vega(), 4)
    
    def call_theta(self): 
        return round((-self.spot * self.N_tag_d1 * self.volatility / (2 * np.sqrt(self.days)) - 
                      self.rate * self.strike * np.exp(-self.rate * self.days) * stats.norm.cdf(self.d2)) / 365, 4)
    
    def put_theta(self): 
        return round((-self.spot * self.N_tag_d1 * self.volatility / (2 * np.sqrt(self.days)) + 
                      self.rate * self.strike * np.exp(-self.rate * self.days) * stats.norm.cdf(-self.d2)) / 365, 4)
    
    def call_rho(self): 
        return round(self.strike * self.days * np.exp(-self.rate * self.days) * stats.norm.cdf(self.d2) / 100, 4)
    
    def put_rho(self): 
        return round(-self.strike * self.days * np.exp(-self.rate * self.days) * stats.norm.cdf(-self.d2) / 100, 4)


if __name__=='__main__': 
    op1 = BS(1800, 1800, 0.01, 30, 0.2, 1)
    op2 = BS(1800, 1790, 0.01, 30, 0.2, 1)
    
    # Example usage with strike price
    print(f"Strike Price: {op1.strike}")
    print(f"Call Price: {op1.call_price()}")
    print(f"Put Price: {op1.put_price()}")
    print(f"Call Delta: {op1.call_delta()}")
    print(f"Put Delta: {op1.put_delta()}")

    print(f"\nStrike Price: {op2.strike}")
    print(f"Call Price: {op2.call_price()}")
    print(f"Put Price: {op2.put_price()}")
    print(f"Call Delta: {op2.call_delta()}")
    print(f"Put Delta: {op2.put_delta()}")