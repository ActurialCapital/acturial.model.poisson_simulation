<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="https://github.com/ActurialCapital/luminar/blob/main/images/img1.png" width="30%" height="30%">
</p>

  <h2 align="center">Luminar</h2>

  <p align="center">
  <b>Modeling indiosyncratic risk</b>
  </p>
 
## 💡 Table of Contents
<br>

* [About the Project](#about-the-project)
  * [Introduction](#introduction)
  * [Model Assumptions](#model-assumptions)
  * [Built With](#built-with)
* [Quick Start](#quick-start)
* [Author](#author)
* [License](#license)

## ⚡ About the Project

### 🎉 Introduction

Idiosyncratic risk (IR) is a type of investment risk that is endemic to an individual asset, a group of assets or a very specific asset class. IR is also referred to as a specific risk or unsystematic risk. Therefore, the opposite of IR is a systematic risk, which is the overall risk that affects all assets, such as fluctuations in the stock market, interest rates, or the entire financial system. While IR is, by definition, irregular and unpredictable, highly individual, or even unique, it can be substantially mitigated or eliminated from a portfolio by using adequate diversification, proper asset allocation or hedging strategies.

Research suggests that IR accounts for most of the variation in the uncertainty surrounding an individual stock over time, rather than market risk, styles, or other factors. IR can be thought of as the factors that affect an asset such as the stock and its underlying company at the microeconomic level. It has little or no correlation with risks that reflect larger macroeconomic forces, such as market risk. Microeconomic factors are those that affect a limited or small portion of the entire economy, and macro forces are those impacting larger segments or the entire economy. 

### 👉 Model assumptions

The Poisson process model for Monte Carlo methods is used to simulate a particular market, taking into account idiosyncrasies:
  - Market returns are independent and identically distributed random variables
  - There is a certain probabilistic number of successful/failing companies that are identifiable - including, but not limited to, earnings surprises, change in competitive environment, management's decisions on financial policy, investment strategy, and operations, supply-chain disruptions, bankruptcies, defaults, profit warnings, lake of demand, political uncertainties...
  - As a consequence, the successful/failing companies are represented by a sharp increase/decrease in stock price and a surge of volatility
  - The number of successful/failing companies follows a Poisson distribution

The Poisson distribution:

<p align="center">
   <img src="https://numpy.org/doc/stable/_images/math/c91108ae66a9a5e2feb9442c67962868e368fdc8.svg">
</p>

For events with an expected separation ![equation](https://numpy.org/doc/stable/_images/math/cefc603e5658facb747581f9567192993f21c7ab.svg) the Poisson distribution ![equation](https://numpy.org/doc/stable/_images/math/4d00b2dcd7c9300ef7b531ec4b19efbd75cf8ea6.svg) describes the probability of k events occurring within the observed interval ![equation](https://numpy.org/doc/stable/_images/math/cefc603e5658facb747581f9567192993f21c7ab.svg).

### 📚 Built With

  - numpy
  - random
  - scipy

## 💥 Quick Start

Import necessary modules:

```
from luminar import simulate
```

Run function **.with_jumps**:

``` 
items = simulate.with_jumps(
    S0=100,
    rf=0.05,
    sigma=0.20,
    n_iter=100,
    n_simul=100,
    t=1,
    l=2,
    mu_y=0.02,
    var_y=0.25,
    K=100
 )
```

As a result, we get a dictionary with keys as:
  - **'simulation'**: n_simul number of simulations for n_iter iterations
  - **'jumps'**: number of jumps created for each random timeseries

For example:

``` 
for i in range(0, 4): items['simulation'][i].plot()
```

<p align="center">
  <img src="https://github.com/ActurialCapital/luminar/blob/main/images/Figure_1.png" width="50%" height="50%">
</p>  

``` 
pd.DataFrame(items['simulation']).stack().hist(bins=100)
```

<p align="center">
  <img src="https://github.com/ActurialCapital/luminar/blob/main/images/Figure_2.png" width="50%" height="50%">
</p>

## 📖 License

This project is licensed under the MIT License
