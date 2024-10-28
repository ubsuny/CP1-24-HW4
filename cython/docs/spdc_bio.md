push by:
11/20
todo:
id applications
basic setup
simulate with qiskit
price equipment?

## Basics
-direct a high-energy pump laser through a nonlinear crystal.
-quantum correlations between the generated photon pairs.
-one photon in the entangled pair (signal) can interact with a sample, while the other (idler) is measured separately.
-analyze the correlated data, (SPDC imaging can create detailed images with enhanced contrast and low noise-- even in low-light or environments with high scattering, absorb, or disp properties)

# Imaging Biological Tissue with SPDC: Possible Benefits
- **Non-Invasive and Low-Intensity**: low-intensity, entangled photon pairs allows for gentle imaging of sensitive tissues (maybe even in vivo?). Minimal tissue damage due to low energy of photons
- **Deep Tissue Penetration**: with near-infrared wavelengths can possibly achieve greater depth penetration than fluorescence methods, reaching depths of **0.5-1 mm**(?? verify) in biological tissues. Might be especially well-suited for imaging layered structures, complex tissues, and thick (or living) samples.

**Concept**
When SPDC photons pass through biological tissue, scattering, absorption, and dispersion occur. This interaction may provide useful information about the tissue’s composition, behavior, or structures by analyzing how quantum correlations are affected. SPDC imaging methods like quantum optical coherence tomography (QOCT) (read more) and ghost imaging (read more) can thus provide depth-resolved representations of complex samples.

### Comparison of SPDC with Electron and Super-Resolution Microscopy
MORE RESEARCH NEEDED...
#### Electron Microscopy (EM)
- **Resolution and Capabilities**: EM (inc SEM and TEM) provides the highest resolution of any imaging technique for biological samples, reaching down to **0.5-2 nm**. It can reveal cellular ultrastructure in fixed samples, visualizing organelles, membranes, and protein complexes in near-atomic detail.
- **Limitations**: Requires extensive sample preparation, including dehydration, staining, and vacuum environments, making it unsuitable for live imaging. Good for imaging static structures, but is invasive and time-intensive.

#### Super-Resolution Fluorescence Microscopy
- **Resolution and Capabilities**: Super-resolution techniques such as STED, PALM, and STORM break the diffraction limit achieving resolutions of **10-50 nm**. They enable live-cell imaging at high resolution, useful for studying protein distributions, molecular interactions, and cellular dynamics.
- **Limitations**: Requires fluorescent labeling, which can introduce challenges for imaging unlabeled structures. Depth penetration is limited to **tens of micrometers**, and the acquisition process can be slower due to the need for high photon counts and precise molecule localization.

### Advantages of Multi-Photon SPDC Imaging
1. **Non-Invasive, Low Phototoxicity**: SPDC photons operate at low intensities, ideal for imaging live or sensitive samples. Reduces photobleaching and photodamage. SPDC imaging is advantageous for studying living tissues or organisms over time with minimal impact on sample integrity.

2. **Enhanced Contrast and Noise Resistance**: SPDC-based methods can leverage quantum correlations to reduce noise and enhance image contrast, even in challenging imaging conditions. Techniques like ghost imaging are resistant to scattering and provide clear images of structures within scattering media, like biological tissues. (needs more research..)

3. **Deeper Penetration in Thick Samples**: With near-infrared wavelengths, multi-photon SPDC imaging can achieve tissue penetration depths of up to **0.5-1 mm**, allowing imaging of complex or thick samples without invasive sectioning. This capability is superior to super-resolution techniques, which are limited in penetration depth. (viability of multiphoton setups? lots of things to figure out here still)

4. **Pushing the Limit EVEN Further**: Some experimental SPDC setups are working toward achieving sub-diffraction resolution using quantum entanglement principles. This could theoretically enable SPDC imaging to reach resolutions similar to super-resolution fluorescence techniques, possibly down to **10-50 nm**, while still maintaining low phototoxicity and deep penetration.

### Practical Considerations in SPDC Imaging
- **Nonlinear Crystal and Pump Source**: SPDC requires a high-energy UV or blue pump laser directed through a nonlinear crystal (like BBO or KDP) to generate entangled photon pairs.
- **Beam Splitter and Delay Line**: A beam splitter separates the signal and idler photons, with an adjustable delay line to control timing and depth resolution.
- **Detection and Coincidence Counting**: Sensitive single-photon detectors and a coincidence counter are necessary to capture quantum correlations accurately. The setup generally occupies a standard optical table, but advances are being made in miniaturizing SPDC setups for practical applications.

### Current Limitations
- **Resolution Constraints**: Although SPDC can achieve micrometer-level resolution, it does not yet match the atomic-level detail of electron microscopy or the near-molecular precision of super-resolution microscopy without specialized setups.
- **Low Photon Flux and Longer Acquisition Times**: SPDC generates fewer photons than classical light sources, resulting in slower acquisition times. This can limit the technique’s practicality for high-speed imaging applications. (potential for clever workarounds?)
