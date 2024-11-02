# Estimating the Age of the Universe

### Purpose

The `age` function takes the Hubble constant as input and calculates an estimated age of the universe. The calculation uses a known conversion factor for megaparsecs (Mpc) to kilometers (km) to transform the Hubble constant from its given units (km/s/Mpc) into a meaningful time scale. Using these parameters we can estimate the age of the universe by calculating the Hubble time.

### Background on the Hubble Constant

- The **Hubble constant** (denoted H0) represents the rate at which galaxies are moving away from Earth per unit distance or we can call it the rate of exmpansion. It’s commonly measured in **km/s per Mpc** (kilometers per second per megaparsec).
- The Hubble constant can be used to estimate the age of the universe because it implies an inverse relationship between time and expansion rate. In essence, a higher Hubble constant would indicate a younger universe, while a lower Hubble constant would suggest an older universe.
- We can estimate the age of the universe with a simple function that takes conversion of megaparsec to kilometer and the Hubble constant and converts it to time in seconds.

### Megaparsec Conversion

We can start by converting a megaparsec to its kilometer equivalent (1 megaparsec = 3.09*10^19 km). This conversion factor allows us to use the Hubble constant (km/s/Mpc) to estimate the universe's age in seconds.

### Time Equation

Since we know that the hubble constant H0 is (km/s)/(3.09*10^9 km) we can plug this into the time equation:
$$ 
{t} = 1/{H}_{0} 
$$
This will then get us out estimated age of the universe in seconds.

## Code Explanation

The code for the `age` function is as follows:
```python
def age(hub_cons):
    """So for this it takes Hubble's constant and outputs the age of the universe."""
    MEGPAR_TO_KM = 3.09 * (10 ** 19)  # Conversion factor for megaparsec to kilometers
    return MEGPAR_TO_KM * (hub_cons ** -1)
```

Plugging in an expansion rate of 70 for the parameter `hub_cons` we can then find the approximate time in seconds of the universe being about 4.4E17 seconds or converting to years, approximately 13,952,308,472 years.