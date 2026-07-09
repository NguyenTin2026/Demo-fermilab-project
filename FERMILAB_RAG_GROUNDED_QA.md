# Fermilab RAG — Verified Grounded Q&A

**241 question–answer pairs**, each verified to be answerable **only** from the Fermilab corpus (`corpus_st7.jsonl`). No outside knowledge is used.

For every pair below, the answer's content is present in the cited source page (*grounding* = fraction of the answer's content words found in that page). The Streamlit app pins each question's source page as Document [1] and refuses to answer when the corpus lacks the evidence, so responses cannot be fabricated.

- Average grounding: **0.92**  ·  median **0.93**  ·  minimum **0.52**

---

### 1. What is Fermilab's primary mission as America's particle physics and accelerator laboratory?

Fermilab's mission is to serve as a world-leader in neutrino and particle physics. It aims to push the frontiers of foundational discovery, open new avenues of science, and transform results into technologies that benefit society.

**Source:** `text_pages/0001_news.fnal.gov` — https://news.fnal.gov  ·  *grounding 1.00*

### 2. What is the Quantum Instrumentation Control Kit (QICK) developed by Fermilab?

The Quantum Instrumentation Control Kit, or QICK, is a compact, customizable, and cost-effective quantum readout and control option developed by Fermilab. It is designed to be used by scientists.

**Source:** `text_pages/0001_news.fnal.gov` — https://news.fnal.gov  ·  *grounding 1.00*

### 3. How do Fermilab's Quantum Instrumentation Control Kit (QICK) and Harmoniqs' Piccolo.jl software contribute to the optimization of qubit control?

Fermilab developed QICK as a quantum readout and control option, while Harmoniqs developed Piccolo.jl as a quantum control and calibration software package. Their developers are integrating these two tools to achieve precise, repeatable qubit control, aiming for better results in less time.

**Source:** `text_pages/0001_news.fnal.gov` — https://news.fnal.gov  ·  *grounding 1.00*

### 4. What is the Master of Science in Physics program specializing in quantum science and technology offered by Fermilab and Northern Illinois University?

The Master of Science in Physics program specializing in quantum science and technology is an innovative graduate program launched by Fermilab and Northern Illinois University. This program combines the expertise of a DOE national laboratory quantum center and a prominent state university to prepare the next generation of quantum experts.

**Source:** `text_pages/0001_news.fnal.gov` — https://news.fnal.gov  ·  *grounding 1.00*

### 5. What is the purpose of Fermilab's collaboration with Harmoniqs regarding the QICK Toolkit?

Fermilab is collaborating with Harmoniqs to integrate its Piccolo.jl software, a quantum control and calibration package, with QICK. This collaboration aims to enable more precise and repeatable qubit manipulation.

**Source:** `text_pages/0001_news.fnal.gov` — https://news.fnal.gov  ·  *grounding 1.00*

### 6. How many scientists and institutions are part of the DUNE collaboration?

The DUNE collaboration includes more than 1,500 scientists. These scientists are from over 220 institutions across 38 countries.

**Source:** `text_pages/0001_news.fnal.gov` — https://news.fnal.gov  ·  *grounding 1.00*

### 7. What significant event related to the DUNE experiment occurred on May 11, 2026?

On May 11, 2026, the first steel beams for the DUNE experiment started to be lowered underground. This event marked a milestone for the international DUNE experiment.

**Source:** `text_pages/0001_news.fnal.gov` — https://news.fnal.gov  ·  *grounding 1.00*

### 8. What is the primary mission of Fermilab as an institution?

Fermilab is America’s particle physics and accelerator laboratory, dedicated to exploring the fundamental nature of the universe. Since 1967, the laboratory has pursued big questions in science, such as what matter is made of, how the universe began, and how it has evolved over time.

**Source:** `text_pages/0003_education.fnal.gov_about` — https://education.fnal.gov/about  ·  *grounding 1.00*

### 9. What topics are covered in the Neutrino Physics kit provided by Fermilab?

The Neutrino Physics kit explores the mysterious behavior and properties of neutrinos. It teaches how Fermilab produces, detects, and studies neutrinos, and also explains how neutrinos are able to oscillate to change their type.

**Source:** `text_pages/0004_education.fnal.gov_program_stem-outreach` — https://education.fnal.gov/program/stem-outreach  ·  *grounding 1.00*

### 10. What is Aleksandra Ćiprijanović's goal for using artificial intelligence in high-energy physics research?

Aleksandra Ćiprijanović, an Early Career Award recipient, aims to create a universal AI analysis framework. This framework will use artificial intelligence to solve the domain shift problem in high-energy physics research, with support from Fermilab's computing capabilities.

**Source:** `text_pages/0006_news.fnal.gov_tag_ai` — https://news.fnal.gov/tag/ai  ·  *grounding 1.00*

### 11. What is Fermilab's role concerning the integration of AI and ML technologies for the DUNE project?

Fermilab leads the DUNE project and recently collaborated on an international workshop hosted by Rice University. This workshop focused on integrating cutting-edge AI and ML technologies to tackle the monumental computational challenges posed by DUNE and to strategize on leveraging AI's transformative capabilities within particle physics.

**Source:** `text_pages/0006_news.fnal.gov_tag_ai` — https://news.fnal.gov/tag/ai  ·  *grounding 1.00*

### 12. What significant milestone did Fermilab's FAST/IOTA accelerator test facility achieve, and what are its implications?

Fermilab’s FAST/IOTA accelerator test facility successfully accelerated and stored its first proton beams. This achievement is a major milestone for next-generation particle accelerator technology R&D, paving the way for breakthroughs in high-intensity beam physics, artificial intelligence applications, and innovations for future experiments like the Deep Underground Neutrino Experiment.

**Source:** `text_pages/0006_news.fnal.gov_tag_ai` — https://news.fnal.gov/tag/ai  ·  *grounding 1.00*

### 13. What is Fermilab's role as America's national laboratory?

Fermi National Accelerator Laboratory is America’s national laboratory for particle physics and accelerator research. Its core scientific mission is to bring the world together to solve the mysteries of matter, energy, space, and time.

**Source:** `text_pages/0008_news.fnal.gov_2026_05_fermilab-leads-multi-lab-ai-initi` — https://news.fnal.gov/2026/05/fermilab-leads-multi-lab-ai-initiative-to-accelerate-design-of-chips-used-in-extreme-environments  ·  *grounding 1.00*

### 14. What is the primary purpose of the SuperCDMS SNOLAB experiment?

The SuperCDMS SNOLAB experiment is a second-generation dark matter search. Its goal is to detect and study dark matter particles.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 1.00*

### 15. Which organizations jointly fund the SuperCDMS SNOLAB experiment?

The SuperCDMS SNOLAB experiment is jointly funded by the U.S. Department of Energy Office of Science, the U.S. National Science Foundation, the Canada Foundation for Innovation, and the Natural Sciences and Engineering Research Council of Canada.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 1.00*

### 16. What is the SNOBOX in the SuperCDMS experiment, and what is its function?

The SNOBOX is a large copper cryostat used in the SuperCDMS experiment. Its function is to house the SuperCDMS detectors.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 1.00*

### 17. What was the significance of the recent milestone event for the DUNE experiment at the Sanford Underground Research Facility?

The milestone event for the Deep Underground Neutrino Experiment (DUNE) at the Sanford Underground Research Facility in South Dakota marked the start of steel beams being lowered underground. These beams are being installed to house DUNE’s massive particle detectors.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 1.00*

### 18. Why is CERN's contribution to the DUNE experiment considered significant?

CERN's contribution is significant because it marks the first time the organization has invested in infrastructure for an experiment located outside of Europe. This demonstrates the tangible impact of international in-kind contributions to the DUNE project.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 1.00*

### 19. What is the mission of the Sanford Underground Research Facility (SURF)?

The mission of the Sanford Underground Research Facility (SURF) is to advance world-class science and inspire learning across generations. It operates as America’s Underground Lab, managed by the South Dakota Science and Technology Authority with funding from the Department of Energy’s Office of Science.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 1.00*

### 20. What technology will the DUNE experiment utilize for its detectors?

The DUNE experiment will use liquid-argon time projection chamber technology for both its near and far detectors. Fermilab's priority is to deliver the first neutrino beam to DUNE by 2031, following the start of underground detector installation.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 1.00*

### 21. What is Anna Grassellino's primary role at Fermilab, and what new federal appointment has she received?

Anna Grassellino serves as the chief technology officer and associate laboratory director for the Technology Directorate at Fermi National Accelerator Laboratory. She has been appointed to the U.S. Department of Energy’s Office of Science Advisory Committee (SCAC) and will also chair its quantum subcommittee.

**Source:** `text_pages/0010_news.fnal.gov_2026_05_anna-grassellino-appointed-to-doe` — https://news.fnal.gov/2026/05/anna-grassellino-appointed-to-doe-office-of-science-advisory-committee  ·  *grounding 1.00*

### 22. How does the collaboration between Fermilab's QICK and Harmoniqs' Piccolo.jl benefit quantum computing?

Fermilab developed the Quantum Instrumentation Control Kit (QICK) for quantum readout and control, and Harmoniqs developed Piccolo.jl software for quantum control and calibration. Their collaboration integrates these tools to achieve precise and repeatable qubit control, which provides better results in less time for quantum computing.

**Source:** `text_pages/0010_news.fnal.gov_2026_05_anna-grassellino-appointed-to-doe` — https://news.fnal.gov/2026/05/anna-grassellino-appointed-to-doe-office-of-science-advisory-committee  ·  *grounding 1.00*

### 23. What is Fermilab's overarching mission?

Fermilab's mission is to bring the world together to solve the mysteries of matter, energy, space, and time.

**Source:** `text_pages/0010_news.fnal.gov_tag_qick` — https://news.fnal.gov/tag/qick  ·  *grounding 1.00*

### 24. How does the Linac Coherent Light Source (LCLS) create X-rays?

The LCLS uses superconducting radio-frequency technology to power an electron beam to high energies. This electron beam is then sent through special magnets called undulators, which make it jiggle and produce X-rays. As the X-rays and electron beam interact, they produce coherent radiation.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 1.00*

### 25. What organizations collaborated to improve the cryomodules for the LCLS high-energy upgrade?

Accelerator experts from SLAC, Jefferson Lab, Cornell University, and Fermilab combined their efforts to improve the cryomodules for the Linac Coherent Light Source (LCLS) high-energy upgrade.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 1.00*

### 26. What is "nitrogen doping" in the context of the LCLS cryomodule upgrade?

In the context of the LCLS cryomodule upgrade, "nitrogen doping" is a process through which the molecular makeup of the walls of the superconducting accelerator cavities was optimized. This technique was developed to improve these components.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 1.00*

### 27. How many cryomodules did Fermilab and Jefferson Lab each contribute to the LCLS high-energy upgrade?

For the LCLS high-energy upgrade, Jefferson Lab contributed 10 cryomodules. Fermilab constructed 14 cryomodules, completing their part of the 24 cryomodules needed for the high-energy upgrade.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 1.00*

### 28. What specific American company is partnering with Fermilab to develop superconducting radio-frequency systems, and what is the goal of this collaboration?

The American company partnering with Fermilab is xLight. Their goal is to develop superconducting radio-frequency (SRF) systems for their semiconductor lithography systems, which will improve semiconductor chips critical for modern technology such as smartphones, computers, and military applications.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 1.00*

### 29. What event did Fermilab celebrate on April 21, 2026?

On April 21, 2026, Fermilab celebrated the birth of the first baby bison of the year. This new addition joined the American bison herd at Fermilab.

**Source:** `text_pages/0013_news.fnal.gov_category_ext_in-the-news` — https://news.fnal.gov/category/ext/in-the-news  ·  *grounding 1.00*

### 30. When was the first baby bison of the spring season born at Fermilab?

The first cinnamon-colored baby bison of the spring season was born at Fermilab on April 21. The new calf is healthy and is staying close to its mother as it takes its first steps.

**Source:** `text_pages/0013_news.fnal.gov_category_ext_in-the-news` — https://news.fnal.gov/category/ext/in-the-news  ·  *grounding 1.00*

### 31. What is a dark photon and how is it related to ordinary photons?

A dark photon is a theorized dark matter particle that the new detector is designed to search for. If it exists, the dark photon would be distantly related to the photon, which is a visible particle of light.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 1.00*

### 32. What is the function of the SQUID coupler within the new quantum detector for dark photons?

The SQUID coupler, or superconducting quantum interference device, acts as a tuner in the quantum detector. It electronically adjusts the frequencies that the connected microwave cavity can scan.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 1.00*

### 33. What is Fermilab's core scientific mission?

Fermilab's core scientific mission is to bring the world together to solve the mysteries of matter, energy, space, and time.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 1.00*

### 34. What is the primary role of Fermilab’s Communication Division?

Fermilab’s Communication Division serves as the link between the laboratory and the local and worldwide communities.

**Source:** `text_pages/0015_news.fnal.gov_newsroom_contact` — https://news.fnal.gov/newsroom/contact  ·  *grounding 1.00*

### 35. What email address should members of the media use for inquiries to Fermilab?

Members of the media should direct their inquiries to media@fnal.gov.

**Source:** `text_pages/0015_news.fnal.gov_newsroom_contact` — https://news.fnal.gov/newsroom/contact  ·  *grounding 1.00*

### 36. What is the current status of the data collection phase for the MicroBooNE experiment?

The MicroBooNE experiment has wrapped up its data-collecting phase. It will now continue to conduct analysis under fresh leadership.

**Source:** `text_pages/0018_news.fnal.gov_2026_05_mark-ross-lonergan-elected-co-spo` — https://news.fnal.gov/2026/05/mark-ross-lonergan-elected-co-spokesperson-for-microboone-collaboration  ·  *grounding 1.00*

### 37. What was the central goal of the MicroBooNE experiment?

The central goal of the MicroBooNE experiment was to follow up on a puzzling result from an earlier experiment called MiniBooNE. MiniBooNE had detected more particle interactions than expected, which suggested the potential existence of new physics.

**Source:** `text_pages/0018_news.fnal.gov_2026_05_mark-ross-lonergan-elected-co-spo` — https://news.fnal.gov/2026/05/mark-ross-lonergan-elected-co-spokesperson-for-microboone-collaboration  ·  *grounding 1.00*

### 38. What is the primary role of Fermi National Accelerator Laboratory (Fermilab) in the U.S.?

Fermi National Accelerator Laboratory (Fermilab) serves as America's national laboratory for particle physics and accelerator research. It is managed by the Fermi Forward Discovery Group for the U.S. Department of Energy Office of Science.

**Source:** `text_pages/0018_news.fnal.gov_2026_05_mark-ross-lonergan-elected-co-spo` — https://news.fnal.gov/2026/05/mark-ross-lonergan-elected-co-spokesperson-for-microboone-collaboration  ·  *grounding 1.00*

### 39. Why are Fermilab and Harmoniqs integrating their quantum tools, QICK and Piccolo.jl?

Fermilab and Harmoniqs are integrating QICK and Piccolo.jl to achieve precise and repeatable qubit control. This collaboration aims to provide better results for quantum computing in less time.

**Source:** `text_pages/0020_news.fnal.gov_tag_partnership` — https://news.fnal.gov/tag/partnership  ·  *grounding 1.00*

### 40. How are Fermilab and NYU Langone Health advancing magnetic resonance imaging (MRI) technology?

Fermilab and NYU Langone Health, both partners in the Superconducting Quantum Materials and Systems Center, are advancing MRI technology by developing Quantitative MRI. This collaboration takes the cornerstone of modern medical diagnostics a step further.

**Source:** `text_pages/0020_news.fnal.gov_tag_partnership` — https://news.fnal.gov/tag/partnership  ·  *grounding 1.00*

### 41. What is the name of the new graduate program launched by Fermilab and Northern Illinois University?

Fermilab and Northern Illinois University are launching a Master of Science in Physics program with a specialization in quantum science and technology. This innovative graduate program aims to prepare the next generation of quantum experts.

**Source:** `text_pages/0021_news.fnal.gov_2026_04_fermilab-teams-up-with-niu-to-lau` — https://news.fnal.gov/2026/04/fermilab-teams-up-with-niu-to-launch-quantum-science-program  ·  *grounding 1.00*

### 42. What is the new Master of Science in Physics program offered by Northern Illinois University in partnership with Fermilab?

The new Master of Science in Physics program at Northern Illinois University offers a specialization in quantum science and technology. This program provides students with the opportunity to conduct research at the SQMS Center, which is led by Fermilab.

**Source:** `text_pages/0021_news.fnal.gov_2026_04_fermilab-teams-up-with-niu-to-lau` — https://news.fnal.gov/2026/04/fermilab-teams-up-with-niu-to-launch-quantum-science-program  ·  *grounding 1.00*

### 43. What is QICK, and which institution developed it?

QICK, or Quantum Instrumentation Control Kit, is a compact, customizable, and cost-effective quantum readout and control option designed for scientists. Fermilab developed the QICK system.

**Source:** `text_pages/0021_news.fnal.gov_2026_04_fermilab-teams-up-with-niu-to-lau` — https://news.fnal.gov/2026/04/fermilab-teams-up-with-niu-to-launch-quantum-science-program  ·  *grounding 1.00*

### 44. What is the purpose of the innovative power-over-fiber system being perfected for the Deep Underground Neutrino Experiment?

The innovative power-over-fiber system is being perfected to enable photon detectors to operate reliably in the challenging cryogenic and high-voltage conditions within the Deep Underground Neutrino Experiment.

**Source:** `text_pages/0022_news.fnal.gov_tag_dune` — https://news.fnal.gov/tag/dune  ·  *grounding 1.00*

### 45. What area of research will Physicist Steven Gardiner pursue with the Deep Underground Neutrino Experiment after receiving his Early Career Award?

Steven Gardiner will explore the low-energy research potential of the Deep Underground Neutrino Experiment. He plans to leverage DUNE's massive detector modules to study elusive particles from outer space, using his background in neutron simulations.

**Source:** `text_pages/0022_news.fnal.gov_tag_dune` — https://news.fnal.gov/tag/dune  ·  *grounding 1.00*

### 46. Who was recently elected as co-spokesperson for the Deep Underground Neutrino Experiment (DUNE) collaboration and what is their role?

Dave Newbold was elected as co-spokesperson of the Deep Underground Neutrino Experiment (DUNE) collaboration on March 17, 2026. His role is to co-lead the largest neutrino experiment in the U.S.

**Source:** `text_pages/0022_news.fnal.gov_tag_dune` — https://news.fnal.gov/tag/dune  ·  *grounding 1.00*

### 47. What role does artificial intelligence play in the national AI Genesis Mission?

Artificial intelligence is central to the Genesis Mission, as it aims to integrate the transformative power of AI across the national research landscape to supercharge innovation. This includes deploying AI to make particle accelerators adaptive and autonomous, and advancing next-generation microelectronics.

**Source:** `text_pages/0027_news.fnal.gov_2026_03_fermilab-drives-progress-for-nati` — https://news.fnal.gov/2026/03/fermilab-drives-progress-for-national-ai-genesis-mission  ·  *grounding 1.00*

### 48. How does the AXESS project aim to speed up chip design?

The AXESS project aims to speed up custom microelectronics chip design by using AI to compress the design process. This technology is expected to reduce the design time from months to minutes, significantly boosting national competitiveness and accelerating the pace of innovation for specialized scientific applications.

**Source:** `text_pages/0027_news.fnal.gov_2026_03_fermilab-drives-progress-for-nati` — https://news.fnal.gov/2026/03/fermilab-drives-progress-for-national-ai-genesis-mission  ·  *grounding 1.00*

### 49. What is Lattice Quantum Chromodynamics, and how does FemtoMind utilize it?

Lattice Quantum Chromodynamics (Lattice QCD) is a theoretical framework physicists use to understand the strong force that binds subatomic quarks together to form protons. The FemtoMind effort applies agentic AI to quicken the complex calculations within Lattice QCD and to uncover new patterns in computer simulations that probe physics at the proton scale.

**Source:** `text_pages/0027_news.fnal.gov_2026_03_fermilab-drives-progress-for-nati` — https://news.fnal.gov/2026/03/fermilab-drives-progress-for-national-ai-genesis-mission  ·  *grounding 1.00*

### 50. What is the primary objective of the Genesis Mission, according to Fermilab's Nhan Tran?

According to Nhan Tran, head of AI coordination at Fermilab, the Genesis Mission aims to integrate data, tools, and expertise from all 17 national laboratories. The goal is to create a unified AI ecosystem that can accelerate scientific breakthroughs beyond what any single lab could achieve on its own.

**Source:** `text_pages/0027_news.fnal.gov_2026_03_fermilab-drives-progress-for-nati` — https://news.fnal.gov/2026/03/fermilab-drives-progress-for-national-ai-genesis-mission  ·  *grounding 1.00*

### 51. How is Fermilab contributing to the Genesis Mission's goals?

Fermilab is making vital contributions to the Genesis Mission by leveraging its expertise to supercharge microelectronics design, enhance particle accelerator research and development, and transform data analysis. The lab also leads a multi-lab AI initiative focused on accelerating the design of custom computer chips for extreme environments.

**Source:** `text_pages/0027_news.fnal.gov_2026_03_fermilab-drives-progress-for-nati` — https://news.fnal.gov/2026/03/fermilab-drives-progress-for-national-ai-genesis-mission  ·  *grounding 1.00*

### 52. What is Olivia Seidel's primary research at Fermilab?

Olivia Seidel, a Ph.D. student within Fermilab’s Microelectronics group, is researching how transistors behave when they get very cold. She is leveraging artificial intelligence for cryogenic transistor modeling to accelerate her research.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 1.00*

### 53. How does the new electronically-tunable quantum detector developed by Fermilab and its collaborators accelerate the search for dark matter?

The new electronically-tunable quantum detector accelerates the search for dark matter by enabling scientists to electronically tune the detector. This allows them to search broader frequency ranges for weak signals produced by dark photons, which are possible dark matter particles, much faster and more precisely than before.

**Source:** `text_pages/0029_news.fnal.gov_tag_dark-matter` — https://news.fnal.gov/tag/dark-matter  ·  *grounding 1.00*

### 54. What is Ryan Linehan's research focus at Fermi National Accelerator Laboratory?

At Fermi National Accelerator Laboratory, postdoctoral researcher Ryan Linehan explores the intersection of quantum information science and particle physics. He studies how particles impact superconducting quantum devices. This work helps advance both quantum computing and dark matter detection.

**Source:** `text_pages/0029_news.fnal.gov_tag_dark-matter` — https://news.fnal.gov/tag/dark-matter  ·  *grounding 1.00*

### 55. What was the scope and process of rock excavation for the DUNE project at the far site?

Excavation work for the DUNE project at the far site began in early 2019 and concluded in February 2024. During this period, almost 800,000 tons of rock were removed from approximately 5,000 feet (1,520 meters) below ground. This rock traveled up the renovated mile-deep Ross shaft at SURF and then along a three-quarter-mile-long above-ground conveyor to the Open Cut, a former mining area in Lead, South Dakota.

**Source:** `text_pages/0007_news.fnal.gov_2026_04_largest-neutrino-experiment-in-th` — https://news.fnal.gov/2026/04/largest-neutrino-experiment-in-the-us-wins-project-of-the-year-award  ·  *grounding 0.97*

### 56. What is the purpose of the TREASURE initiative regarding physics data?

The TREASURE initiative aims to make vast datasets more accessible for groundbreaking research. It standardizes data from current and retired particle colliders, like the Large Hadron Collider and the Tevatron, to create AI-ready representations for cross-experiment analysis. This program also converts research papers, datasets, and code into user-friendly forms for scientists searching for physics beyond the Standard Model.

**Source:** `text_pages/0027_news.fnal.gov_2026_03_fermilab-drives-progress-for-nati` — https://news.fnal.gov/2026/03/fermilab-drives-progress-for-national-ai-genesis-mission  ·  *grounding 0.97*

### 57. How does the new quantum detector achieve its sensitivity for detecting weak signals from dark photons?

The new quantum detector achieves its sensitivity by placing an electrically-tunable superconducting quantum interference device, or SQUID, inside a three-dimensional microwave cavity. The SQUID's superconductance means it has no resistance to energy, allowing it to pick up even the faintest signals from dark photons. The detector is also housed in a dilution refrigerator at cryogenic temperatures and shielded from low-frequency magnetic fields.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 0.97*

### 58. What is the purpose of the XCOM system developed by Fermilab and Stanford University researchers?

The XCOM system, developed by Fermilab and Stanford University researchers, is a novel network designed to synchronize quantum instrumentation and facilitate low-latency communication. It connects multiple QICK boards in a mesh network to enable synchronized operation and deterministic communication between distributed control electronics, addressing a key challenge in scaling quantum computing systems.

**Source:** `text_pages/0032_news.fnal.gov_tag_qick` — https://news.fnal.gov/tag/qick  ·  *grounding 0.97*

### 59. How do Fermilab's QICK and Harmoniqs' Piccolo.jl contribute to the advancement of qubit control optimization?

Fermilab developed the Quantum Instrumentation Control Kit (QICK) as a compact, customizable, and cost-effective quantum readout and control option. Harmoniqs, a quantum computing software company, developed Piccolo.jl as a quantum control and calibration software package. Their developers are integrating these two tools to achieve precise, repeatable qubit control, aiming to provide better results in less time.

**Source:** `text_pages/0016_news.fnal.gov_newsroom_news` — https://news.fnal.gov/newsroom/news  ·  *grounding 0.97*

### 60. What is the Accelerating eXtreme Environment Specs-to-Silicon (AXESS) project and what is its primary objective?

The AXESS project, which stands for Accelerating eXtreme Environment Specs-to-Silicon, is a multi-lab AI initiative led by Fermi National Accelerator Laboratory. Its primary objective is to use artificial intelligence to significantly reduce the design times of custom computer chips for use in extreme temperature, high-radiation, and ultra-fast environments.

**Source:** `text_pages/0008_news.fnal.gov_2026_05_fermilab-leads-multi-lab-ai-initi` — https://news.fnal.gov/2026/05/fermilab-leads-multi-lab-ai-initiative-to-accelerate-design-of-chips-used-in-extreme-environments  ·  *grounding 0.97*

### 61. What does the ICARUS milestone enable for the Short-Baseline Neutrino Program at Fermilab?

The ICARUS milestone paves the way to probe sterile-neutrino oscillations for the full Short-Baseline Neutrino Program at Fermilab. The first results demonstrate the data's excellent quality and suitability for physics analyses, along with the maturity of the software tools for event selection, fitting, and detector simulation.

**Source:** `text_pages/0012_news.fnal.gov_category_newsroom_press-release` — https://news.fnal.gov/category/newsroom/press-release  ·  *grounding 0.97*

### 62. What is the significance of the recent milestone achieved by the ICARUS experiment?

The recent milestone by the ICARUS experiment is significant because it paves the way to probe sterile-neutrino oscillations for the full Short-Baseline Neutrino Program at Fermilab. The initial results from ICARUS demonstrate excellent data quality, suitability for physics analyses, and the maturity of its software tools for event selection, fitting, and detector simulation.

**Source:** `text_pages/0018_news.fnal.gov_2026_05_mark-ross-lonergan-elected-co-spo` — https://news.fnal.gov/2026/05/mark-ross-lonergan-elected-co-spokesperson-for-microboone-collaboration  ·  *grounding 0.97*

### 63. What does Fermilab Director Norbert Holtkamp believe is the significance of the Genesis Mission?

Fermilab Director Norbert Holtkamp views the Genesis Mission as a "once-in-a-generation opportunity" to transform how America does science. He believes that combining AI, advanced computing, and national laboratory capabilities will accelerate discovery, strengthen scientific infrastructure, and enhance the quality and efficiency of work across Fermilab and the broader U.S. national lab complex.

**Source:** `text_pages/0027_news.fnal.gov_2026_03_fermilab-drives-progress-for-nati` — https://news.fnal.gov/2026/03/fermilab-drives-progress-for-national-ai-genesis-mission  ·  *grounding 0.97*

### 64. Why is Fermilab considered well-equipped to contribute to the Genesis Mission's goals?

Fermilab is considered well-equipped due to its expertise in high-energy physics, advanced computing, accelerator and quantum technologies, and microelectronics design. The lab also brings decades of experience navigating complex challenges through large-scale collaborations with national laboratory partners, academia, and industry.

**Source:** `text_pages/0027_news.fnal.gov_2026_03_fermilab-drives-progress-for-nati` — https://news.fnal.gov/2026/03/fermilab-drives-progress-for-national-ai-genesis-mission  ·  *grounding 0.97*

### 65. What does "from the ground up" signify for building deep cryogenic models for transistors at Fermilab?

In this context, building a model "from the ground up" means starting from the material properties of the transistor itself, rather than adapting a room-temperature approximation. The machine learning model would infer the underlying physics directly from lab measurements, offering a fundamentally different and more powerful approach than adjusting a pre-existing framework.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.97*

### 66. How will the DUNE experiment capture neutrino interactions with high precision?

The DUNE experiment will capture neutrino interactions with high precision by using detectors that cool thousands of tons of liquid argon to approximately minus 300 degrees Fahrenheit. This super-cooled liquid argon is housed within enormous cryostats, with each of the two planned modules containing 17,000 tons of liquid argon nearly a mile underground at SURF.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 0.96*

### 67. What is the purpose of the XCOM network developed by Fermilab and Stanford University researchers?

The XCOM network, developed by Fermilab and Stanford University researchers, is designed to synchronize quantum instrumentation and facilitate low-latency communication. It connects multiple QICK boards in a mesh network, enabling synchronized operation and deterministic communication between distributed control electronics to address quantum control bottlenecks.

**Source:** `text_pages/0010_news.fnal.gov_tag_qick` — https://news.fnal.gov/tag/qick  ·  *grounding 0.96*

### 68. What is Fermilab scientist Yao Lu's research focused on, and what award supports this work?

Fermilab scientist Yao Lu's research is focused on harnessing quantum entanglement to search for dark matter. He is building a scalable superconducting cavity array designed to detect faint signals from mysterious dark photons with unprecedented speed and sensitivity. This work is supported by a DOE Early Career Award.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.96*

### 69. How does the liquid-argon time projection chamber technology used by MicroBooNE identify particles, similar to watching the wake left by a boat?

The liquid-argon time projection chamber allows scientists to identify exactly what kind of particle is being detected and where it came from by recording trails left by charged particles in liquid argon. This is analogous to watching the wake left by a boat on calm water and identifying the type of boat that created it.

**Source:** `text_pages/0018_news.fnal.gov_2026_05_mark-ross-lonergan-elected-co-spo` — https://news.fnal.gov/2026/05/mark-ross-lonergan-elected-co-spokesperson-for-microboone-collaboration  ·  *grounding 0.96*

### 70. How does the new electronically tunable quantum detector improve the search for dark matter?

The new electronically tunable quantum detector improves the search for dark matter by allowing scientists to electronically tune itself and search broader frequency ranges for weak signals produced by dark photons, which are possible dark matter particles. This enables a much faster and more precise search than previously possible.

**Source:** `text_pages/0001_news.fnal.gov` — https://news.fnal.gov  ·  *grounding 0.96*

### 71. Why are Fermilab researchers enhancing neural networks and developing an open-source framework for hardware design?

Fermilab researchers are enhancing neural networks to boost the potential of AI in revolutionizing particle physics. They are also developing an open-source framework for hardware capable of making split-second decisions, with the goal of prioritizing the enormous volumes of data produced by ambitious physics experiments.

**Source:** `text_pages/0021_news.fnal.gov_2026_04_fermilab-teams-up-with-niu-to-lau` — https://news.fnal.gov/2026/04/fermilab-teams-up-with-niu-to-launch-quantum-science-program  ·  *grounding 0.96*

### 72. What is the structural layout of the LBNF caverns for the DUNE experiment's far detectors?

The Long-Baseline Neutrino Facility (LBNF) consists of three long cut-out caverns. Two of these caverns are designed to house two far detector modules each, placed end-to-end. The third cavern is dedicated to housing cryogenics equipment and other essential utilities that keep the powerful detectors running.

**Source:** `text_pages/0007_news.fnal.gov_2026_04_largest-neutrino-experiment-in-th` — https://news.fnal.gov/2026/04/largest-neutrino-experiment-in-the-us-wins-project-of-the-year-award  ·  *grounding 0.96*

### 73. What role does CERN play in the development and construction of the DUNE experiment?

CERN plays a pivotal role in the DUNE experiment by developing its prototype detectors and providing the two enormous cryostats for the experiment itself. Additionally, CERN contributes approximately 10 million pounds of structural steel beams as an in-kind contribution for the support structure of DUNE's massive particle detector modules.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 0.96*

### 74. How does the time required for the machine learning approach compare to the conventional method for predicting optimal physics parameters from deep cryogenic transistor measurement data at Fermilab?

Once trained, the machine learning model can predict optimal physics parameters in approximately 120 milliseconds. In contrast, the conventional approach can take anywhere from weeks to months, depending on the transistor. This represents an enormous speed-up in the modeling process.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.96*

### 75. Why was the DUNE project recognized with a UCA Project of the Year Award?

The DUNE project received a UCA Project of the Year Award for its monumental scale and impressive safety record. The project logged over one million hours during construction without a lost-time incident, demonstrating insight and understanding of underground construction and overcoming unusual problems.

**Source:** `text_pages/0007_news.fnal.gov_2026_04_largest-neutrino-experiment-in-th` — https://news.fnal.gov/2026/04/largest-neutrino-experiment-in-the-us-wins-project-of-the-year-award  ·  *grounding 0.96*

### 76. What is the primary goal of the Genesis Mission project at Fermilab?

The primary goal of the Genesis Mission project is to build a framework that uses AI to accelerate the chip-design process. This aims to dramatically reduce the time from chip specification to fabrication from months to weeks. The framework also helps designers make optimal decisions at each step of the design process.

**Source:** `text_pages/0008_news.fnal.gov_2026_05_fermilab-leads-multi-lab-ai-initi` — https://news.fnal.gov/2026/05/fermilab-leads-multi-lab-ai-initiative-to-accelerate-design-of-chips-used-in-extreme-environments  ·  *grounding 0.96*

### 77. What is the XCOM network developed by Fermilab and Stanford University researchers, and what challenge does it address?

The XCOM network is a novel network developed by Fermilab and Stanford University researchers. It is designed to synchronize quantum instrumentation and facilitate low-latency communication, addressing a key challenge in scaling quantum computing systems related to low-latency, predictable communication across control hardware.

**Source:** `text_pages/0012_news.fnal.gov_tag_quantum` — https://news.fnal.gov/tag/quantum  ·  *grounding 0.96*

### 78. What is the purpose of the Master of Science in Physics program launched by Fermilab and Northern Illinois University?

The Master of Science in Physics program, a collaboration between Fermilab and Northern Illinois University, specializes in quantum science and technology. Its purpose is to prepare the next generation of quantum experts by combining the expertise of a DOE national laboratory quantum center and a prominent state university.

**Source:** `text_pages/0020_news.fnal.gov_tag_partnership` — https://news.fnal.gov/tag/partnership  ·  *grounding 0.96*

### 79. Why did Rice University host an international workshop for the DUNE project?

Rice University hosted an international workshop for the DUNE project to integrate cutting-edge AI and ML technologies. The workshop aimed to tackle the monumental computational challenges posed by DUNE and to strategize on leveraging AI's transformative capabilities within the field of particle physics.

**Source:** `text_pages/0022_news.fnal.gov_tag_dune` — https://news.fnal.gov/tag/dune  ·  *grounding 0.96*

### 80. What is the primary objective of the MOAT collaboration?

The primary objective of the Multi-Office particle Accelerator Team (MOAT) collaboration is to advance accelerator science by using AI. This effort aims to support more efficient operations and streamlined accelerator research and development, which is expected to shorten commissioning timelines and reduce operating costs.

**Source:** `text_pages/0027_news.fnal.gov_2026_03_fermilab-drives-progress-for-nati` — https://news.fnal.gov/2026/03/fermilab-drives-progress-for-national-ai-genesis-mission  ·  *grounding 0.96*

### 81. What is a key component of the Deep Underground Neutrino Experiment's innovative hybrid near detector?

A key component of the Deep Underground Neutrino Experiment's innovative hybrid near detector is a liquid-argon time projection chamber. This element's design and data analysis tools have been refined and validated through an active prototyping program.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 0.96*

### 82. What is the Superconducting Quantum Materials and Systems Center (SQMS)?

The Superconducting Quantum Materials and Systems Center (SQMS) is one of the five U.S. Department of Energy National Quantum Information Science Research Centers. It is led by Fermi National Accelerator Laboratory and operates as a collaboration of more than 40 partner institutions, including national labs, academia, and industry.

**Source:** `text_pages/0010_news.fnal.gov_2026_05_anna-grassellino-appointed-to-doe` — https://news.fnal.gov/2026/05/anna-grassellino-appointed-to-doe-office-of-science-advisory-committee  ·  *grounding 0.96*

### 83. What is Quantitative MRI, and which organizations are collaborating on its development?

Quantitative MRI is an advancement that takes magnetic resonance imaging, a cornerstone of modern medical diagnostics, a step further. This technology is being developed through a collaboration between Fermilab and NYU Langone Health, both of which are partners in the Superconducting Quantum Materials and Systems Center.

**Source:** `text_pages/0021_news.fnal.gov_2026_04_fermilab-teams-up-with-niu-to-lau` — https://news.fnal.gov/2026/04/fermilab-teams-up-with-niu-to-launch-quantum-science-program  ·  *grounding 0.96*

### 84. What are the future applications of the technology developed by Fermilab for the LCLS upgrade?

The technology developed by Fermilab for the high-energy upgrade of the superconducting accelerator for SLAC’s X-ray laser, LCLS, will be transferred to industry for semiconductor-chip production. Additionally, this technology will be used in the Proton Improvement Plan-II, which is one of Fermilab’s flagship projects.

**Source:** `text_pages/0001_news.fnal.gov` — https://news.fnal.gov  ·  *grounding 0.95*

### 85. What topics are covered in the "Intro to Fermilab Science" STEM Outreach Kit?

The "Intro to Fermilab Science" STEM Outreach Kit explores various areas of Fermilab science. These include fundamental elementary particles, neutrino beam production and oscillations, particle accelerators, quantum science, dark matter, and dark energy.

**Source:** `text_pages/0004_education.fnal.gov_program_stem-outreach` — https://education.fnal.gov/program/stem-outreach  ·  *grounding 0.95*

### 86. What is the primary objective of the U.S. Department of Energy's Genesis Mission?

The primary objective of the Genesis Mission is to significantly reduce the design times of custom computer chips for use in extreme temperature, high-radiation, and ultra-fast environments. This is achieved by leveraging the power of artificial intelligence.

**Source:** `text_pages/0006_news.fnal.gov_tag_ai` — https://news.fnal.gov/tag/ai  ·  *grounding 0.95*

### 87. What award did the Long-Baseline Neutrino Facility/Deep Underground Neutrino Experiment (LBNF/DUNE) receive?

The Long-Baseline Neutrino Facility/Deep Underground Neutrino Experiment (LBNF/DUNE) was awarded the prestigious 2026 Project of the Year Award by the Underground Construction Association. This recognition was for completing a significant and challenging underground construction project in the United States.

**Source:** `text_pages/0007_news.fnal.gov_2026_04_largest-neutrino-experiment-in-th` — https://news.fnal.gov/2026/04/largest-neutrino-experiment-in-the-us-wins-project-of-the-year-award  ·  *grounding 0.95*

### 88. How do interferometers, such as the one featured in the MAGIS-100 exhibit at Fermilab, function to create an interference pattern?

Interferometers work by using beam-splitters, which reflect and transmit light simultaneously, causing photons to take two different paths. Mirrors at the ends of these paths reflect the beams back to the beam-splitter, where they recombine and interfere with each other, creating an interference pattern.

**Source:** `text_pages/0008_education.fnal.gov_lederman-science-center` — https://education.fnal.gov/lederman-science-center  ·  *grounding 0.95*

### 89. What technology will the Deep Underground Neutrino Experiment (DUNE) use for its detectors?

The Deep Underground Neutrino Experiment (DUNE) will utilize liquid-argon time projection chamber technology for both its near and far detectors. An active prototyping program has been refining and validating the design of this key element for the smaller detector.

**Source:** `text_pages/0016_news.fnal.gov_newsroom_news` — https://news.fnal.gov/newsroom/news  ·  *grounding 0.95*

### 90. Why is cryogenic transistor modeling becoming increasingly critical for various fields, according to Fermilab research?

Cryogenic transistor modeling is becoming increasingly critical because it is essential infrastructure for quantum computing, particle physics, and space technology. Twenty years ago, it wasn't a primary focus, but now the demand for this capability is only going to grow.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.95*

### 91. What are SMSPDs, and what is their potential role in particle physics research according to a Fermilab-led study?

SMSPDs are superconducting microwire single photon detectors. According to a Fermilab-led study, these ultrasensitive devices show great promise for particle physics research of the future, specifically for tracking high-energy particles and detecting dark matter.

**Source:** `text_pages/0029_news.fnal.gov_tag_dark-matter` — https://news.fnal.gov/tag/dark-matter  ·  *grounding 0.95*

### 92. What is a cryomodule in the context of the LCLS high-energy upgrade?

In the context of the LCLS high-energy upgrade, a cryomodule is an accelerating structure. Fermilab developed and built these superconducting cryomodules, which are a key part of the upgrade designed to enhance the power and performance of the Linac Coherent Light Source X-ray laser.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.95*

### 93. How does the MicroBooNE detector track neutrinos?

The MicroBooNE detector uses 170 tons of liquid argon chilled to nearly minus 300 degrees Fahrenheit. When a neutrino collides with an argon atom in the detector, it produces a burst of charged particles, which leave trails in the liquid argon that the detector records in fine detail.

**Source:** `text_pages/0018_news.fnal.gov_2026_05_mark-ross-lonergan-elected-co-spo` — https://news.fnal.gov/2026/05/mark-ross-lonergan-elected-co-spokesperson-for-microboone-collaboration  ·  *grounding 0.95*

### 94. Why is Fermilab hosting the national symposium titled ‘Exploring the Quantum Universe’?

Fermilab is hosting the ‘Exploring the Quantum Universe’ symposium to bring together experts from the quantum information science community. This event underscores Fermilab’s increasing emphasis on Quantum Information Science (QIS) research and aligns with the United States' expanding leadership in quantum technology.

**Source:** `text_pages/0020_news.fnal.gov_tag_partnership` — https://news.fnal.gov/tag/partnership  ·  *grounding 0.95*

### 95. What are Superconducting Nanowire Single-Photon Detectors (SNSPDs) and what are they used for?

SNSPDs are thin superconducting films that are designed to detect single particles of light. These detectors are used for particle detection and precision measurements, and they require electronics that can function effectively at deep cryogenic temperatures.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.95*

### 96. What major milestone did the DUNE experiment recently achieve at Fermilab?

The DUNE experiment recently marked a major milestone at its far site, the Sanford Underground Research Facility in South Dakota. This event signified the start of steel beams being lowered underground to construct the housing for DUNE’s massive particle detectors.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.95*

### 97. Where is the DUNE experiment's detector being constructed, and what engineering work has been completed there?

The DUNE experiment's detector is being constructed nearly 1,600 meters below the surface of South Dakota. Workers have removed 800,000 tons of rock and built two giant caverns to house the world's largest underground cryogenic detector.

**Source:** `text_pages/0008_news.fnal.gov_category_ext_in-the-news` — https://news.fnal.gov/category/ext/in-the-news  ·  *grounding 0.95*

### 98. Why is the LCLS high-energy upgrade significant for X-ray laser beams?

The LCLS high-energy upgrade is significant because it enables X-ray laser beams that are 10,000 times brighter and have pulses arriving up to a million times per second. This upgrade doubles the energy of the beam and more than doubles the maximum X-ray energy, greatly enhancing the laser's capabilities.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.95*

### 99. What major milestone was recently marked for the Deep Underground Neutrino Experiment at its far site?

A major milestone for the Deep Underground Neutrino Experiment's far site involved the start of lowering steel beams underground. These beams will house DUNE's massive particle detectors at the Sanford Underground Research Facility in South Dakota.

**Source:** `text_pages/0022_news.fnal.gov_tag_dune` — https://news.fnal.gov/tag/dune  ·  *grounding 0.95*

### 100. How does the collaboration between Northwestern and Fermilab using NEXUS qubit data advance quantum calibration?

The collaboration between Northwestern and Fermilab uses NEXUS qubit data to build a new AI benchmark for quantum calibration. This data has enabled the training of NVIDIA Ising Calibration, which is a vision language model designed to automate the calibration of quantum processors.

**Source:** `text_pages/0032_news.fnal.gov_tag_qick` — https://news.fnal.gov/tag/qick  ·  *grounding 0.95*

### 101. What significant milestone did the Deep Underground Neutrino Experiment (DUNE) achieve recently at the Sanford Underground Research Facility?

The Deep Underground Neutrino Experiment (DUNE) marked the start of steel beams being lowered underground at its far site in the Sanford Underground Research Facility in South Dakota. These beams are intended to house DUNE’s massive particle detectors.

**Source:** `text_pages/0001_news.fnal.gov` — https://news.fnal.gov  ·  *grounding 0.95*

### 102. What is the primary function of the three massive caverns constructed for the Deep Underground Neutrino Experiment (DUNE)?

The three massive caverns constructed for the Deep Underground Neutrino Experiment (DUNE) are designed to house massive detectors and an entire laboratory system. This underground facility is dedicated to conducting cutting-edge neutrino research.

**Source:** `text_pages/0007_news.fnal.gov_2026_04_largest-neutrino-experiment-in-th` — https://news.fnal.gov/2026/04/largest-neutrino-experiment-in-the-us-wins-project-of-the-year-award  ·  *grounding 0.95*

### 103. How do the DUNE detectors compare to other underground cryogenic systems globally?

The DUNE detectors are anticipated to be the largest underground cryogenic system in the world. The construction of the three caverns for the new research facility created an underground area close to the size of eight soccer fields.

**Source:** `text_pages/0007_news.fnal.gov_2026_04_largest-neutrino-experiment-in-th` — https://news.fnal.gov/2026/04/largest-neutrino-experiment-in-the-us-wins-project-of-the-year-award  ·  *grounding 0.95*

### 104. What is the primary goal of the Proton Improvement Plan-II (PIP-II) project at Fermilab?

The primary goal of the Proton Improvement Plan-II (PIP-II) project is to build a new, powerful linear accelerator. This accelerator is specifically designed to create the world's most intense beam of neutrinos for the Deep Underground Neutrino Experiment.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 0.95*

### 105. What is Norbert Holtkamp's role at Fermilab?

Norbert Holtkamp is establishing clear priorities and a disciplined strategy for Fermilab. His leadership aims to align the laboratory with the nation’s most ambitious research goals and position it for long-term success.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 0.95*

### 106. How does the Deep Underground Neutrino Experiment (DUNE) relate to the MicroBooNE experiment?

The MicroBooNE experiment served as a proving ground for the Deep Underground Neutrino Experiment (DUNE), which is a much larger future project. Lessons learned from MicroBooNE and the broader Short-Baseline Neutrino Program, including advances in computing algorithms, detector hardware, and machine learning techniques, are being incorporated into DUNE's design. DUNE will also use liquid-argon detectors, similar to MicroBooNE's technology, but on a much larger scale, weighing thousands of tons.

**Source:** `text_pages/0018_news.fnal.gov_2026_05_mark-ross-lonergan-elected-co-spo` — https://news.fnal.gov/2026/05/mark-ross-lonergan-elected-co-spokesperson-for-microboone-collaboration  ·  *grounding 0.95*

### 107. What is the SQMS Center and its role within the U.S. Department of Energy's national initiative?

The SQMS Center, led by Fermilab, is one of five DOE quantum information science research centers. These centers are integral to the U.S. Department of Energy's national initiative aimed at developing and deploying the world's most powerful quantum computers and sensors.

**Source:** `text_pages/0021_news.fnal.gov_2026_04_fermilab-teams-up-with-niu-to-lau` — https://news.fnal.gov/2026/04/fermilab-teams-up-with-niu-to-launch-quantum-science-program  ·  *grounding 0.95*

### 108. What specific milestone did Fermilab mark for the DUNE experiment on May 7, 2026?

On May 7, 2026, Fermilab marked the start of steel beams being lowered underground at the Sanford Underground Research Facility in South Dakota. These beams are intended to house DUNE’s massive particle detectors.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 0.94*

### 109. What is the primary goal of the state-of-the-art qubit detector designed by Fermilab researchers?

The primary goal of the state-of-the-art qubit detector designed by Fermilab researchers is to search for very weak signals from dark photons. Researchers aimed to build a detector more sensitive than any previous ones, which they achieved.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 0.94*

### 110. With which firm is Fermilab partnering to develop a water treatment system targeting PFAS?

Fermilab is partnering with Proficio Consultancy, a Chicagoland firm, to develop a specialized water treatment system. This system uses beams of electrons to destroy harmful chemicals, specifically PFAS, in water.

**Source:** `text_pages/0020_news.fnal.gov_tag_partnership` — https://news.fnal.gov/tag/partnership  ·  *grounding 0.94*

### 111. Which organizations jointly fund the SuperCDMS SNOLAB project?

The SuperCDMS SNOLAB project is jointly funded by the U.S. Department of Energy Office of Science, the U.S. National Science Foundation, the Canada Foundation for Innovation, and the Natural Sciences and Engineering Research Council of Canada.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.94*

### 112. How does the Proton Improvement Plan-II (PIP-II) project contribute to the Deep Underground Neutrino Experiment?

The Proton Improvement Plan-II (PIP-II) project is building a new, powerful linear accelerator. This accelerator will create the world's most intense beam of neutrinos, which is essential for the Deep Underground Neutrino Experiment.

**Source:** `text_pages/0022_news.fnal.gov_tag_dune` — https://news.fnal.gov/tag/dune  ·  *grounding 0.94*

### 113. What is the purpose of the PIP-II accelerator project at Fermilab?

The PIP-II accelerator project at Fermilab will be used to send a beam of neutrinos through the Earth for the Deep Underground Neutrino Experiment. This powerful new accelerator's construction is a successful collaboration between the United States and United Kingdom.

**Source:** `text_pages/0022_news.fnal.gov_tag_dune` — https://news.fnal.gov/tag/dune  ·  *grounding 0.94*

### 114. What does Fermilab's STEM outreach program offer to schools, libraries, and community events?

Fermilab's STEM outreach programs are ideal for schools, libraries, and community events. They highlight Fermilab science through engaging hands-on activities and exciting demonstrations.

**Source:** `text_pages/0002_education.fnal.gov` — https://education.fnal.gov  ·  *grounding 0.94*

### 115. How does the X-ray production process in the LCLS compare to that of a standard laser pointer?

Genfa Wu explains that the LCLS uses a process similar to a laser pointer, but it operates within an accelerator. The key difference is that instead of producing visible light, the LCLS generates coherent photons in the X-ray spectrum.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.94*

### 116. What is the focus of the partnership between Fermilab and xLight Inc.?

The partnership between Fermilab and xLight Inc. focuses on producing advanced semiconductors in the United States. This will be achieved by leveraging extreme ultraviolet light and accelerator technology.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.94*

### 117. What is the purpose of the quantum subcommittee that Anna Grassellino chairs?

Anna Grassellino of Fermilab chairs the quantum subcommittee as part of her role on the DOE Office of Science Advisory Committee. This subcommittee is specifically tasked with advancing national quantum goals.

**Source:** `text_pages/0016_news.fnal.gov_newsroom_news` — https://news.fnal.gov/newsroom/news  ·  *grounding 0.94*

### 118. What is the Accelerating eXtreme Environment Specs-to-Silicon (AXES) project led by Fermilab aiming to achieve?

The AXES project, a Genesis Mission initiative led by Fermilab, aims to advance microelectronics in extreme environments where industry expertise and investment are scarce. It uses new machine learning work to build a complete deep cryogenic model for transistors. These transistors are highly sought after for quantum information science and high energy physics applications at 4 kelvin.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.94*

### 119. Which specific hardware system is mentioned in connection with real-time quantum control using QICK?

Real-time quantum control using QICK is implemented on the iWave Zynq™ UltraScale+™ RFSoC system on module. This system is part of an emerging technologies partnership.

**Source:** `text_pages/0032_news.fnal.gov_tag_qick` — https://news.fnal.gov/tag/qick  ·  *grounding 0.94*

### 120. What are the real-world applications that benefit from knowledge about transistor behavior at cryogenic temperatures?

Knowledge about transistor behavior at cryogenic temperatures benefits several areas, including trapped ion quantum computing, superconducting nanowire single-photon detectors (SNSPDs), and the readout and control of superconducting qubits. Additionally, it has applications in particle physics, such as the DUNE at LBNF neutrino experiment, and for deep space satellite designers.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.94*

### 121. How is Fermilab contributing to the U.S. Department of Energy's Genesis Mission?

Fermilab contributes to the Genesis Mission in several ways, including leading a multi-lab AI initiative to accelerate the design of chips for extreme environments. Fermilab researchers, like Olivia Seidel, also use AI to probe transistor behavior in extreme cold, and the lab coordinates with other national labs to develop AI tools for particle accelerators as part of the mission.

**Source:** `text_pages/0006_news.fnal.gov_tag_ai` — https://news.fnal.gov/tag/ai  ·  *grounding 0.93*

### 122. Why was the Long-Baseline Neutrino Facility/Deep Underground Neutrino Experiment (LBNF/DUNE) project given the Project of the Year Award?

The LBNF/DUNE project received the Project of the Year Award for successfully completing a significant and challenging underground construction project with minimal issues and an impeccable safety record. Fermilab Director Norbert Holtkamp commended the engineering teams for their success in designing, excavating, and constructing the colossal caverns.

**Source:** `text_pages/0007_news.fnal.gov_2026_04_largest-neutrino-experiment-in-th` — https://news.fnal.gov/2026/04/largest-neutrino-experiment-in-the-us-wins-project-of-the-year-award  ·  *grounding 0.93*

### 123. Why did the LBNF project receive the 2026 Project of the Year award?

The LBNF project was awarded the 2026 Project of the Year by the Underground Construction Association because its teams successfully removed over 800,000 tons of rock from an extreme depth.

**Source:** `text_pages/0008_news.fnal.gov_category_ext_in-the-news` — https://news.fnal.gov/category/ext/in-the-news  ·  *grounding 0.93*

### 124. Why is SNOLAB situated deep underground and maintained as a clean room for experiments like SuperCDMS?

SNOLAB is located deep underground to shield experiments from cosmic rays that could produce false positives in detectors. As a class-2000 clean room, it also protects experiments from trace radioactivity found in common materials like dirt. These conditions are crucial for studying rare phenomena such as dark matter.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.93*

### 125. What is the primary purpose of the PIP-II linear accelerator, a flagship project at Fermilab?

The PIP-II linear accelerator is being built by assembling superconducting radio-frequency cryomodules. Its primary purpose is to power the forthcoming Deep Underground Neutrino Experiment (DUNE).

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.93*

### 126. Why is the partnership between Northern Illinois University and Fermilab significant for students enrolled in the new Master's program?

The partnership creates a powerful opportunity for NIU students to study at a leading-edge facility where discovery happens daily, leveraging the research, expertise, and facilities available at Fermilab's SQMS Center. This collaboration, combining interactive coursework with hands-on research, equips students with the essential skills and experience for careers in quantum science and technology.

**Source:** `text_pages/0021_news.fnal.gov_2026_04_fermilab-teams-up-with-niu-to-lau` — https://news.fnal.gov/2026/04/fermilab-teams-up-with-niu-to-launch-quantum-science-program  ·  *grounding 0.93*

### 127. How does the AXESS project aim to improve the process of designing custom computer chips for scientific research?

The AXESS project aims to improve chip design by leveraging artificial intelligence to accelerate the development process. Custom-designing specialized chips typically involves an iterative, time-intensive process that can take many months or even years, and AI is used to significantly reduce these design times.

**Source:** `text_pages/0008_news.fnal.gov_2026_05_fermilab-leads-multi-lab-ai-initi` — https://news.fnal.gov/2026/05/fermilab-leads-multi-lab-ai-initiative-to-accelerate-design-of-chips-used-in-extreme-environments  ·  *grounding 0.93*

### 128. How do Fermilab's QICK and Harmoniqs' Piccolo.jl contribute to qubit control optimization when integrated?

Fermilab developed the Quantum Instrumentation Control Kit, or QICK, as a compact, customizable, and cost-effective quantum readout and control option. Harmoniqs developed Piccolo.jl as a quantum control and calibration software package. Together, their integration aims to achieve precise, repeatable qubit control, providing better results in less time.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 0.93*

### 129. What does the acronym MAGIS-100 stand for, and what kind of instrument is it at Fermilab?

MAGIS-100 stands for Matter-wave Atomic Gradiometer Interferometric Sensor. It is described as a long-baseline atom interferometer at Fermilab.

**Source:** `text_pages/0008_education.fnal.gov_lederman-science-center` — https://education.fnal.gov/lederman-science-center  ·  *grounding 0.93*

### 130. Why is Fermi National Accelerator Laboratory particularly well-suited to lead the AXESS project?

Fermilab is well-suited to lead the AXESS project because its particle detectors must function in some of the most extreme environments, requiring custom designs for radiation, cryogenic temperatures, and speed. This has allowed Fermilab to establish deep expertise in microelectronics for extreme environments and to develop tools for integrating AI onto chips.

**Source:** `text_pages/0008_news.fnal.gov_2026_05_fermilab-leads-multi-lab-ai-initi` — https://news.fnal.gov/2026/05/fermilab-leads-multi-lab-ai-initiative-to-accelerate-design-of-chips-used-in-extreme-environments  ·  *grounding 0.93*

### 131. What are the physical dimensions of each planned detector module for the DUNE experiment?

Each of the two planned DUNE detector modules will be roughly the size of a five-story building. Specifically, they will measure 216 feet long, 62 feet wide, and 60 feet high.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 0.93*

### 132. Why is accurate transistor modeling at 4 Kelvin important for the Genesis Mission project?

Accurate transistor modeling at 4 Kelvin, which is approximately minus 450 degrees Fahrenheit, is important for the Genesis Mission project because it is crucial for the operation of chips in quantum environments. This capability supports the project's initial focus on designing chips used to control quantum sensors, devices, and systems.

**Source:** `text_pages/0008_news.fnal.gov_2026_05_fermilab-leads-multi-lab-ai-initi` — https://news.fnal.gov/2026/05/fermilab-leads-multi-lab-ai-initiative-to-accelerate-design-of-chips-used-in-extreme-environments  ·  *grounding 0.92*

### 133. Which organizations partnered with Fermilab to scale U.S. Quantum Control Technology?

Fermilab partnered with the Department of Energy (DOE) and Qblox to scale U.S. Quantum Control Technology. This partnership was highlighted on November 19, 2025.

**Source:** `text_pages/0010_news.fnal.gov_tag_qick` — https://news.fnal.gov/tag/qick  ·  *grounding 0.92*

### 134. How does the SuperCDMS experiment detect dark matter particles?

The SuperCDMS experiment employs 10-centimeter-diameter silicon and germanium crystals, which are photolithographically patterned with sensors. The detection method relies on the belief that dark matter particles will scatter off the nuclei within these crystals, producing a type of vibration called a phonon that the sensors can then detect.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.92*

### 135. Why is the DUNE experiment considered a world-leading and flagship project for the United States?

The DUNE experiment is considered a world-leading and flagship project because it is the largest scientific project supported by the DOE Office of Science and the largest in the United States. It aims to explore fundamental questions about the nature of matter, the evolution of the universe, and the origin of matter-antimatter asymmetry by studying neutrinos.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 0.92*

### 136. Why were Fermilab's contributions to the LCLS upgrade projects considered crucial for the lab's other endeavors?

According to Sam Posen, associate lab director, Fermilab's work on the LCLS upgrade projects was a major accomplishment because it was critical for developing the capabilities and confidence necessary to execute the PIP-II project. Furthermore, these efforts fostered partnerships with industry, allowing Fermilab to apply its research for public benefit.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.92*

### 137. How do the dark matter search methods of Fermilab scientist Yao Lu and the team developing the tunable quantum detector differ?

Fermilab scientist Yao Lu is building a scalable superconducting cavity array to detect faint signals from dark photons by harnessing quantum entanglement. In contrast, the team developing the tunable quantum detector created an electronically-tunable quantum detector that significantly speeds up the search for dark photons.

**Source:** `text_pages/0012_news.fnal.gov_tag_quantum` — https://news.fnal.gov/tag/quantum  ·  *grounding 0.92*

### 138. What is Steven Gardiner's research at the Deep Underground Neutrino Experiment (DUNE) focused on?

Steven Gardiner's research at the Deep Underground Neutrino Experiment (DUNE) is focused on advancing low-energy neutrino research and exploring the experiment's potential in this area. He aims to leverage DUNE's massive detector modules, applying his background in neutron simulations, to study elusive particles from outer space.

**Source:** `text_pages/0018_news.fnal.gov_2026_05_mark-ross-lonergan-elected-co-spo` — https://news.fnal.gov/2026/05/mark-ross-lonergan-elected-co-spokesperson-for-microboone-collaboration  ·  *grounding 0.92*

### 139. Why is Siemens Digital Industries Software involved in the Genesis Mission?

Siemens Digital Industries Software is involved in the Genesis Mission to provide industrial-grade hardware design solutions. By uniting Siemens' proven technologies with the breakthrough science at Fermilab and other DOE labs, they aim to accelerate the creation of new chips for extreme environments.

**Source:** `text_pages/0008_news.fnal.gov_2026_05_fermilab-leads-multi-lab-ai-initi` — https://news.fnal.gov/2026/05/fermilab-leads-multi-lab-ai-initiative-to-accelerate-design-of-chips-used-in-extreme-environments  ·  *grounding 0.92*

### 140. Where is the SuperCDMS experiment located?

The SuperCDMS experiment is located deep underground in a nickel mine outside of Sudbury, Canada. It is specifically housed within the SNOLAB facility.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.92*

### 141. What is the namesake experiment of SNOLAB, and what is its current state?

SNOLAB's namesake experiment is the Nobel Prize-winning Sudbury Neutrino Observatory, or SNO. This experiment has since been upgraded and is currently known as SNO+.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.92*

### 142. What was Fermilab's main contribution to the LCLS high-energy upgrade?

Fermilab's main contribution to the LCLS high-energy upgrade was building and delivering the final component it provided for the superconducting accelerator. Specifically, they produced superconducting cryomodules, which are crucial accelerating structures for the Linac Coherent Light Source (LCLS) at SLAC National Accelerator Laboratory.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.92*

### 143. What are the primary responsibilities of a co-spokesperson for a large scientific collaboration like MicroBooNE?

Spokespeople for large scientific collaborations, such as MicroBooNE, help set research priorities, ensure experiments run smoothly, and represent the teams to the outside world.

**Source:** `text_pages/0018_news.fnal.gov_2026_05_mark-ross-lonergan-elected-co-spo` — https://news.fnal.gov/2026/05/mark-ross-lonergan-elected-co-spokesperson-for-microboone-collaboration  ·  *grounding 0.92*

### 144. How do transistors behave differently at deep cryogenic temperatures compared to room temperature?

At deep cryogenic temperatures below 4 Kelvin, it takes a significantly higher voltage to switch a transistor on. In contrast, at room temperature, a specific voltage is applied, and the transistor turns on. This shift means the entire curve of the transistor's behavior changes at extreme cold.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.92*

### 145. Why are Fermilab and Harmoniqs integrating QICK with Piccolo.jl software?

Fermilab and Harmoniqs are integrating QICK with Harmoniqs' Piccolo.jl software to achieve more precise and repeatable qubit manipulation. This collaboration aims to provide better results in less time by combining Fermilab's quantum readout and control option with Harmoniqs' quantum control and calibration package.

**Source:** `text_pages/0032_news.fnal.gov_tag_qick` — https://news.fnal.gov/tag/qick  ·  *grounding 0.92*

### 146. What is the primary scientific objective of the Superconducting Quantum Materials and Systems Center (SQMS) at Fermilab?

The primary scientific objective of the SQMS Center is to bring transformational advances in the field of quantum information science. It aims to engineer multiqubit quantum processor platforms based on state-of-the-art qubits and superconducting technologies, and to build a quantum computer and new quantum sensors at Fermilab.

**Source:** `text_pages/0010_news.fnal.gov_2026_05_anna-grassellino-appointed-to-doe` — https://news.fnal.gov/2026/05/anna-grassellino-appointed-to-doe-office-of-science-advisory-committee  ·  *grounding 0.91*

### 147. What is the primary purpose of the new electronically tunable quantum detector developed by scientists at Fermilab and collaborating institutions?

The primary purpose of the new electronically tunable quantum detector is to search broader frequency ranges for weak signals produced by dark photons, which are possible dark matter particles. This new detector allows for much faster and more precise searches than previously possible.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 0.91*

### 148. What is the primary objective of the quantum science and technology program established by Fermilab and NIU?

The primary objective of the quantum science and technology program is to prepare the next generation of quantum experts. Students will acquire tangible skills and experiences directly linked to Fermilab’s science goals, enabling them to become subject matter experts in the quantum field.

**Source:** `text_pages/0021_news.fnal.gov_2026_04_fermilab-teams-up-with-niu-to-lau` — https://news.fnal.gov/2026/04/fermilab-teams-up-with-niu-to-launch-quantum-science-program  ·  *grounding 0.91*

### 149. Why is understanding how transistors behave in extreme cold important for Olivia Seidel's research?

Understanding how transistors behave in extreme cold is crucial because emerging technologies, such as quantum computers and satellites in outer space, require electronics that can function at cryogenic temperatures. At these extremely cold conditions, transistors behave very differently than they do at room temperature.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.91*

### 150. What biological principles are covered in the Energy and Ecosystems: Prairie, Water, and Woods teacher workshop at Fermilab?

This teacher workshop at Fermilab covers biological principles and teaches educators how to use standard ecological measurement techniques. These techniques help students investigate, assess, and compare different habitats, such as prairies, water bodies, and woods.

**Source:** `text_pages/0002_education.fnal.gov` — https://education.fnal.gov  ·  *grounding 0.91*

### 151. What is the primary mission of Fermilab?

Fermilab's primary mission is to bring the world together to solve the mysteries of matter, energy, space, and time.

**Source:** `text_pages/0002_education.fnal.gov` — https://education.fnal.gov  ·  *grounding 0.91*

### 152. What is the purpose of the Education and Public Engagement (EPE) department at Fermilab?

The purpose of the Education and Public Engagement department at Fermilab is to share the science of Fermilab with audiences through active engagement and education. It also showcases the arts and promotes stewardship of the environment, aiming to improve public understanding and appreciation of the natural world and Fermilab’s mission.

**Source:** `text_pages/0003_education.fnal.gov_about` — https://education.fnal.gov/about  ·  *grounding 0.91*

### 153. Why is the Proton Improvement Plan-II (PIP-II) project crucial for the Deep Underground Neutrino Experiment?

The Proton Improvement Plan-II (PIP-II) project is crucial for the Deep Underground Neutrino Experiment because it is building a new, powerful linear accelerator. This accelerator is designed to create the world’s most intense beam of neutrinos specifically for the DUNE experiment, which will then send them through the Earth.

**Source:** `text_pages/0007_news.fnal.gov_2026_04_largest-neutrino-experiment-in-th` — https://news.fnal.gov/2026/04/largest-neutrino-experiment-in-the-us-wins-project-of-the-year-award  ·  *grounding 0.91*

### 154. What is the primary mission of the Lederman Science Center at Fermilab?

The mission of the Lederman Science Center is to communicate Fermilab’s leading-edge science with the public. It also aims to showcase the site’s environment and architecture by hosting programs for K-12 students, educators, and learners of all ages and backgrounds.

**Source:** `text_pages/0008_education.fnal.gov_lederman-science-center` — https://education.fnal.gov/lederman-science-center  ·  *grounding 0.90*

### 155. What is the purpose of the 10 million pounds of steel beams being moved underground for the DUNE experiment?

The 10 million pounds of steel beams are being moved a mile underground to build the structural elements that will form DUNE’s detector components. These steel cryostat materials are essential for housing the experiment's massive particle detectors.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 0.90*

### 156. What major milestone did the DUNE experiment achieve on May 7, 2026?

On May 7, 2026, the Deep Underground Neutrino Experiment (DUNE) marked the start of lowering steel beams underground. These beams are intended to house DUNE's massive particle detectors at the far site located at the Sanford Underground Research Facility in South Dakota.

**Source:** `text_pages/0012_news.fnal.gov_category_newsroom_press-release` — https://news.fnal.gov/category/newsroom/press-release  ·  *grounding 0.90*

### 157. What is the significance of the breakthrough achieved by Fermilab and MIT Lincoln Laboratory in quantum computing?

The breakthrough by Fermilab and MIT Lincoln Laboratory, in partnership with national quantum research centers, is significant as it represents a key step towards realizing scalable quantum computers. Researchers used cryoelectronics to control ion traps, which enabled this advancement.

**Source:** `text_pages/0012_news.fnal.gov_category_newsroom_press-release` — https://news.fnal.gov/category/newsroom/press-release  ·  *grounding 0.90*

### 158. What was the significant event that recently took place at the far site of the Deep Underground Neutrino Experiment?

An event at the far site of the Deep Underground Neutrino Experiment, located at the Sanford Underground Research Facility in South Dakota, marked the start of steel beams being lowered underground. These beams are intended to house DUNE’s massive particle detectors.

**Source:** `text_pages/0016_news.fnal.gov_newsroom_news` — https://news.fnal.gov/newsroom/news  ·  *grounding 0.90*

### 159. How do the Fermilab Expert Speaker Request and the STEM Outreach Kits differ in their delivery of science content?

The Fermilab Expert Speaker Request program provides presentations, typically one hour long, where an expert shares their work with an audience. In contrast, the STEM Outreach Kits are designed for large-scale events such as Open Houses or STEM Fairs, offering multiple hands-on activities and demos that are facilitated by Fermilab Expert staff.

**Source:** `text_pages/0004_education.fnal.gov_program_stem-outreach` — https://education.fnal.gov/program/stem-outreach  ·  *grounding 0.90*

### 160. What was the main topic of Mark Adams' public lecture?

Mark Adams' public lecture focused on the search for hidden chambers using cosmic-ray muons.

**Source:** `text_pages/0006_news.fnal.gov_search` — https://news.fnal.gov/search  ·  *grounding 0.90*

### 161. What is the primary objective of the DUNE experiment?

The DUNE experiment aims to study the behavior of mysterious particles known as neutrinos. Through this research, scientists hope to answer some of the biggest questions about our universe, such as why it is composed of matter, how exploding stars create black holes, and if neutrinos are connected to dark matter or other undiscovered particles.

**Source:** `text_pages/0007_news.fnal.gov_2026_04_largest-neutrino-experiment-in-th` — https://news.fnal.gov/2026/04/largest-neutrino-experiment-in-the-us-wins-project-of-the-year-award  ·  *grounding 0.90*

### 162. What recent event marked a significant milestone for the Deep Underground Neutrino Experiment (DUNE) at its far site?

An event at the far site of the Deep Underground Neutrino Experiment (DUNE) at the Sanford Underground Research Facility in South Dakota marked the beginning of steel beams being lowered underground. These steel beams are intended to house DUNE’s massive particle detectors.

**Source:** `text_pages/0007_news.fnal.gov_2026_04_largest-neutrino-experiment-in-th` — https://news.fnal.gov/2026/04/largest-neutrino-experiment-in-the-us-wins-project-of-the-year-award  ·  *grounding 0.90*

### 163. What is the scale of the international DUNE collaboration in terms of scientists and institutions?

The international DUNE collaboration includes more than 1,500 scientists from over 220 institutions. These institutions are located across 38 countries worldwide.

**Source:** `text_pages/0008_news.fnal.gov_category_ext_in-the-news` — https://news.fnal.gov/category/ext/in-the-news  ·  *grounding 0.90*

### 164. What kind of research does Olivia Seidel conduct at Fermilab using artificial intelligence?

Fermilab researcher Olivia Seidel uses artificial intelligence to investigate how transistors behave in extreme cold. Her work leverages Fermilab's extensive knowledge in microelectronics and cryogenic devices to support the key objectives of the Genesis Mission.

**Source:** `text_pages/0027_news.fnal.gov_2026_03_fermilab-drives-progress-for-nati` — https://news.fnal.gov/2026/03/fermilab-drives-progress-for-national-ai-genesis-mission  ·  *grounding 0.90*

### 165. What is the primary function of the Fermilab-developed QICK quantum control system?

The QICK quantum control system, developed by Fermilab, links up with the QASMTrans quantum compilation framework. Its main function is to bridge the gap between logical circuits and the underlying hardware, enabling real-time quantum control.

**Source:** `text_pages/0032_news.fnal.gov_tag_qick` — https://news.fnal.gov/tag/qick  ·  *grounding 0.90*

### 166. Under what conditions might Fermilab staff remove comments from their official social media accounts?

Fermilab staff may remove comments if they contain obscene, indecent, or profane language, or include threats or defamatory statements. Comments containing hate speech directed at race, color, sex, sexual orientation, national origin, ethnicity, age, religion, or disability are also subject to removal. Additionally, comments promoting or endorsing specific commercial services or products, or containing sensitive or personally identifiable information, can be removed.

**Source:** `text_pages/0008_news.fnal.gov_newsroom_social-media` — https://news.fnal.gov/newsroom/social-media  ·  *grounding 0.90*

### 167. Why is it important for circuit designers to understand how transistors behave at cryogenic temperatures?

It is crucial because if circuit designers are unaware of how transistors shift at cryogenic temperatures, the entire circuit can fail or consume significantly more power than intended. In a cryogenic environment, excess power generates excess heat, which can cause decoherence in quantum systems and disrupt electronics used to detect neutrinos in liquid-argon environments.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.90*

### 168. Why did the DUNE experiment receive the Project of the Year Award?

The DUNE experiment, which is the largest neutrino experiment in the United States, was named the Project of the Year by the Underground Construction Association. It received this award for successfully completing a significant and challenging underground construction project with little or no issues.

**Source:** `text_pages/0001_news.fnal.gov` — https://news.fnal.gov  ·  *grounding 0.89*

### 169. Why does Fermilab's Education and Public Engagement department believe it is important to connect audiences to the laboratory's mission?

Fermilab's Education and Public Engagement department believes that the knowledge gained at Fermilab is essential to understanding our world. They connect audiences to Fermilab's mission to improve their understanding and appreciation of the natural world and the laboratory's scientific endeavors.

**Source:** `text_pages/0003_education.fnal.gov_about` — https://education.fnal.gov/about  ·  *grounding 0.89*

### 170. What are some of the official social media platforms where users can connect with Fermilab?

Users can connect with Fermilab on several official social media platforms, including X/Twitter, Facebook, Instagram, LinkedIn, YouTube, and Threads. These platforms provide updates and news from around the laboratory.

**Source:** `text_pages/0008_news.fnal.gov_newsroom_social-media` — https://news.fnal.gov/newsroom/social-media  ·  *grounding 0.89*

### 171. Why was the LBNF/DUNE experiment recognized as the Project of the Year by the Underground Construction Association?

The LBNF/DUNE experiment, the largest neutrino experiment in the United States, was named Project of the Year for completing a significant and challenging underground construction project. This award acknowledged its success in doing so with little or no issues.

**Source:** `text_pages/0012_news.fnal.gov_category_newsroom_press-release` — https://news.fnal.gov/category/newsroom/press-release  ·  *grounding 0.89*

### 172. What recognition did the LBNF project receive for its underground construction work?

The LBNF project received the 2026 Project of the Year award from the Underground Construction Association. This award was given to the teams who removed over 800,000 tons of rock from nearly 1,600 meters below the surface of South Dakota.

**Source:** `text_pages/0013_news.fnal.gov_category_ext_in-the-news` — https://news.fnal.gov/category/ext/in-the-news  ·  *grounding 0.89*

### 173. How are Fermilab researchers utilizing artificial intelligence to advance particle physics?

Fermilab researchers are utilizing artificial intelligence by supercharging neural networks to boost AI's potential to revolutionize particle physics. They are also developing an open-source framework for hardware that can make split-second decisions, aiming to prioritize the vast amounts of data generated by physics experiments.

**Source:** `text_pages/0006_news.fnal.gov_tag_ai` — https://news.fnal.gov/tag/ai  ·  *grounding 0.89*

### 174. What is the purpose of the Department of Energy's Genesis Mission?

The Department of Energy's Genesis Mission is a national mission dedicated to accelerating science through the application of artificial intelligence. The AXESS project is developing proofs of concept to support the goals of this mission.

**Source:** `text_pages/0008_news.fnal.gov_2026_05_fermilab-leads-multi-lab-ai-initi` — https://news.fnal.gov/2026/05/fermilab-leads-multi-lab-ai-initiative-to-accelerate-design-of-chips-used-in-extreme-environments  ·  *grounding 0.89*

### 175. Why are 4.5 million kilograms of steel beams being moved underground for the DUNE experiment?

The 4.5 million kilograms of steel beams are being moved underground to hold DUNE's detectors in place. This process is a significant part of installing the detector structures for the massive neutrino experiment.

**Source:** `text_pages/0008_news.fnal.gov_category_ext_in-the-news` — https://news.fnal.gov/category/ext/in-the-news  ·  *grounding 0.89*

### 176. What was Fermilab's primary role in the LCLS high-energy upgrade?

Fermilab's primary role in the LCLS high-energy upgrade involved developing the enabling technologies at the core of the cryomodules, in addition to building them. Fermilab was the Designer of Record for the cryomodules and innovated new approaches for their improvement.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.89*

### 177. Why was the installation of the first steel beams for the DUNE experiment considered a major milestone?

The installation of the first steel beams for the DUNE experiment was considered a major milestone because it marked the start of moving 4.5 million kilograms of steel beams underground. These beams are essential for holding DUNE's detectors in place.

**Source:** `text_pages/0013_news.fnal.gov_category_ext_in-the-news` — https://news.fnal.gov/category/ext/in-the-news  ·  *grounding 0.89*

### 178. What specific aspects of quantum mechanics will students in the Fermilab-NIU quantum science program learn to leverage?

Students in the Fermilab-NIU quantum science program will learn to manipulate, fabricate, and advance tools and technologies that leverage key features of quantum mechanics. These features include superposition, entanglement, and interference.

**Source:** `text_pages/0021_news.fnal.gov_2026_04_fermilab-teams-up-with-niu-to-lau` — https://news.fnal.gov/2026/04/fermilab-teams-up-with-niu-to-launch-quantum-science-program  ·  *grounding 0.89*

### 179. When will the inaugural class for the Fermilab-NIU quantum science program begin taking classes and start research with Fermilab?

The inaugural class for the Fermilab-NIU quantum science program will begin taking classes in the fall semester of 2026. Students are scheduled to start their research activities with Fermilab in the summer of 2027.

**Source:** `text_pages/0021_news.fnal.gov_2026_04_fermilab-teams-up-with-niu-to-lau` — https://news.fnal.gov/2026/04/fermilab-teams-up-with-niu-to-launch-quantum-science-program  ·  *grounding 0.89*

### 180. What role did Fermilab play in the development of the SuperCDMS experiment?

Fermilab led the design and fabrication of several critical components for the SuperCDMS experiment, including the cryogenic system, the warm electronics, associated infrastructure, and the calibration system. Additionally, Fermilab contributed the seismic platform, which supports the entire experiment and absorbs shock from seismic events, similar to a car's suspension system.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.88*

### 181. How is Fermilab's use of machine learning similar to its past automation efforts?

Fermilab's current use of machine learning is similar to how it once automated wire bonding, which was a precise and painstaking manual process. In both cases, machines take over these tasks, allowing skilled people to focus on more challenging problems and accelerating scientific progress.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.88*

### 182. What is the difference in scope between the U.S. Department of Energy’s Office of Science Advisory Committee (SCAC) and the quantum subcommittee that Anna Grassellino chairs?

The SCAC provides broad independent advice to the DOE Office of Science on overall scientific priorities and major scientific and technical issues. In contrast, the quantum subcommittee, chaired by Anna Grassellino, has a more focused scope, specifically tasked with advancing national quantum goals, assessing quantum information science, and guiding efforts toward error-corrected quantum computers by 2028.

**Source:** `text_pages/0010_news.fnal.gov_2026_05_anna-grassellino-appointed-to-doe` — https://news.fnal.gov/2026/05/anna-grassellino-appointed-to-doe-office-of-science-advisory-committee  ·  *grounding 0.88*

### 183. What is QICK, and what was Fermilab's intention in developing it?

QICK, which stands for the Quantum Instrumentation Control Kit, was developed by Fermilab. It was designed to serve as a compact, customizable, and cost-effective quantum readout and control option specifically for scientists.

**Source:** `text_pages/0016_news.fnal.gov_newsroom_news` — https://news.fnal.gov/newsroom/news  ·  *grounding 0.88*

### 184. What is the main function of the U.S. Department of Energy’s Office of Science Advisory Committee (SCAC)?

The SCAC is a federal advisory body that provides independent advice to the DOE Office of Science. Its main function is to offer guidance on major scientific and technical issues, including scientific priorities, strategies, emerging opportunities, and cross-cutting initiatives.

**Source:** `text_pages/0010_news.fnal.gov_2026_05_anna-grassellino-appointed-to-doe` — https://news.fnal.gov/2026/05/anna-grassellino-appointed-to-doe-office-of-science-advisory-committee  ·  *grounding 0.88*

### 185. Why was the MicroBooNE detector specifically built to distinguish between electrons and single photons?

The MicroBooNE detector was built specifically to distinguish between electrons and single photons because the earlier MiniBooNE experiment could not determine which of these particles caused an excess signal. This distinction is crucial as each possibility would point to a completely different explanation for the observed particle interactions.

**Source:** `text_pages/0018_news.fnal.gov_2026_05_mark-ross-lonergan-elected-co-spo` — https://news.fnal.gov/2026/05/mark-ross-lonergan-elected-co-spokesperson-for-microboone-collaboration  ·  *grounding 0.88*

### 186. What is the frequency of the Fermilab Frontiers public newsletter?

The Fermilab Frontiers public newsletter is delivered to subscribers once a month.

**Source:** `text_pages/0007_news.fnal.gov_newsroom_subscribe-to-fermilab-frontiers` — https://news.fnal.gov/newsroom/subscribe-to-fermilab-frontiers  ·  *grounding 0.88*

### 187. Why is the SuperCDMS SNOLAB experiment cooled to an extremely low temperature?

The SuperCDMS SNOLAB experiment is cooled to a temperature colder than outer space. This extreme cooling is necessary for the superconducting detectors to become operational and function as intended.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.88*

### 188. How does SuperCDMS SNOLAB relate to previous CDMS experiments?

SuperCDMS SNOLAB is an "even bigger upgrade" to the original CDMS experiments. It follows the Fermilab-led CDMS at the Soudan Underground Laboratory and its successor, SuperCDMS Soudan, which ceased operations in 2015.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.88*

### 189. How many scientists and institutions are involved in the DUNE collaboration?

The DUNE collaboration includes more than 1,500 scientists. These scientists are affiliated with over 220 institutions across 38 countries.

**Source:** `text_pages/0013_news.fnal.gov_category_ext_in-the-news` — https://news.fnal.gov/category/ext/in-the-news  ·  *grounding 0.88*

### 190. What are the future applications of the technology developed by Fermilab for the LCLS-II X-ray laser upgrade?

The technology developed by Fermilab for the high-energy upgrade of the superconducting accelerator for SLAC’s X-ray laser, LCLS, has two main future applications. It will be transferred to industry for semiconductor-chip production, and it will also be used in the Proton Improvement Plan-II, one of Fermilab’s flagship projects.

**Source:** `text_pages/0016_news.fnal.gov_newsroom_news` — https://news.fnal.gov/newsroom/news  ·  *grounding 0.88*

### 191. How does flux tuning enable the new quantum detector to 'listen to' different frequencies?

Flux tuning works by applying electromagnetic flux to a SQUID, which precisely controls its ability to oppose changes in electricity flowing through it, similar to an electronic pendulum. This action changes how quickly the SQUID device moves. Since the SQUID is coupled to a microwave cavity, changes in the SQUID correspondingly alter the speed of the cavity, allowing it to detect and respond to different frequencies.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 0.87*

### 192. How do the SuperCDMS experiment and the CMS experiment at CERN contribute differently to the search for dark matter?

The SuperCDMS experiment contributes to the search for dark matter by directly preparing to search for dark matter using its detectors after reaching ultracold operating temperatures and calibration. In contrast, the CMS experiment at CERN is building a new detector for the High-Luminosity Large Hadron Collider to unravel chaotic particle collisions and identify particles based on their speeds, which could indirectly help unmask dark matter.

**Source:** `text_pages/0029_news.fnal.gov_tag_dark-matter` — https://news.fnal.gov/tag/dark-matter  ·  *grounding 0.87*

### 193. What are the main disadvantages of conventional mechanical tuning methods compared to flux tuning for quantum detectors at ultracold temperatures?

Conventional mechanical tuning methods require physically changing the shape of a cavity or adding mechanical parts, which is problematic for qubit-based detectors operating at ultracold temperatures, as parts can seize and break. Furthermore, mechanical parts generate significant heat, creating noise that obscures signals and diminishes the ability to read quantum information. In contrast, flux tuning generates very little heat, preserving coherence and overcoming these challenges.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 0.87*

### 194. Why is it challenging for scientists to find dark matter?

Finding dark matter is challenging for several reasons. Scientists do not know its exact composition, leading to a broad range of particle masses and signal frequencies to search. Additionally, dark matter interacts infrequently with ordinary matter and light, requiring extremely sensitive detectors to capture its very weak signals.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 0.87*

### 195. Why does Fermilab utilize artificial intelligence in its research?

Fermilab utilizes artificial intelligence to lay the groundwork for future researchers so they don't have to spend years on tasks that a well-trained model can complete quickly. This approach aims to make science move faster by freeing skilled people to focus on harder problems, rather than replacing the science itself.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.87*

### 196. Why are Fermilab and Harmoniqs integrating QICK and Piccolo.jl?

Fermilab and Harmoniqs are integrating QICK and Piccolo.jl to achieve precise and repeatable qubit control. This partnership aims to provide better results in less time for quantum computing by combining their respective open-source tools.

**Source:** `text_pages/0010_news.fnal.gov_tag_qick` — https://news.fnal.gov/tag/qick  ·  *grounding 0.86*

### 197. Why are Fermilab researchers working to scale up the new quantum detector technology for dark matter searches?

Researchers are working to scale up the detector technology to significantly expand its scanning capabilities. By combining multiple cavities with a single tunable element, they can simultaneously scan a much wider frequency range, potentially 50 times wider, and achieve full dark photon coverage within reach.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 0.86*

### 198. When was the public lecture by Mark Adams, discussing the search for hidden chambers using cosmic-ray muons, scheduled?

The public lecture by Mark Adams was scheduled for August 11, 2022.

**Source:** `text_pages/0006_news.fnal.gov_search` — https://news.fnal.gov/search  ·  *grounding 0.86*

### 199. What is the function of Fermilab's FAST/IOTA particle accelerator research and development test platform?

Fermilab's FAST/IOTA particle accelerator research and development test platform is utilized to discover methods for incorporating artificial intelligence into accelerator operations. This platform helps explore how AI can be integrated to improve the functioning of accelerators.

**Source:** `text_pages/0027_news.fnal.gov_2026_03_fermilab-drives-progress-for-nati` — https://news.fnal.gov/2026/03/fermilab-drives-progress-for-national-ai-genesis-mission  ·  *grounding 0.86*

### 200. How does the Genesis Mission project's AI-driven chip design process differ from traditional chip design methods?

Traditionally, chips are designed independently in stages by different experts, often leading to issues in subsequent stages and relying on slow, manually operated tools. In contrast, the Genesis Mission project uses AI to integrate all design stages, ensuring decisions optimize the entire design and eliminating traditional bottlenecks. This integration significantly speeds up the overall process.

**Source:** `text_pages/0008_news.fnal.gov_2026_05_fermilab-leads-multi-lab-ai-initi` — https://news.fnal.gov/2026/05/fermilab-leads-multi-lab-ai-initiative-to-accelerate-design-of-chips-used-in-extreme-environments  ·  *grounding 0.85*

### 201. How does the journey for scientists to reach the underground SNOLAB facility compare to a typical city commute?

While both involve leaving on a schedule, the journey to SNOLAB differs significantly from a city commute. Scientists take a cramped, dark elevator, known as a cage, more than a mile below Earth's surface in four minutes. The rapid descent causes pressure changes that can hurt ears if not swallowed frequently, and workers remain underground for about 10 hours.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.85*

### 202. How do Fermilab and CERN compare in terms of their roles in particle physics?

Fermilab is America’s national laboratory for particle physics and accelerator research, managed by the Fermi Forward Discovery Group for the U.S. Department of Energy Office of Science. CERN, on the other hand, is the European Organization for Nuclear Research and is one of the world's leading laboratories for particle physics, located on the French-Swiss border. Both are major centers for particle physics, serving different geographical and organizational scopes.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 0.85*

### 203. How will the technology developed for the LCLS upgrade benefit other projects and industries?

The technology developed for the LCLS upgrade will benefit other projects and industries in two key ways. It will be transferred to industry for use in semiconductor-chip production. Additionally, this technology will be utilized in the Proton Improvement Plan-II (PIP-II), one of Fermilab's own flagship projects.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.85*

### 204. Why was Fermilab's experience in building LCLS-II High Energy cryomodules considered vital for the Proton Improvement Plan-II (PIP-II)?

Fermilab's experience with the LCLS-II High Energy cryomodules was vital for PIP-II because it served as perfect practice for assembling the SRF cryomodules needed for Fermilab's new linear accelerator. The personnel who assembled and tested the LCLS cryomodules are now applying that gained experience and confidence to the PIP-II cryomodules.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.85*

### 205. What is the purpose of the Saturday Morning Physics program at Fermilab?

The Saturday Morning Physics (SMP) program at Fermilab is designed to connect high school students with Fermilab science. It is specifically recommended for students.

**Source:** `text_pages/0002_education.fnal.gov` — https://education.fnal.gov  ·  *grounding 0.85*

### 206. How does the "Electricity and Magnetism" STEM Outreach Kit facilitate learning about these concepts?

The "Electricity and Magnetism" STEM Outreach Kit provides activities that allow participants to explore how electrical currents and magnets interact. Through these activities, individuals learn to create magnetic fields from electrical currents and vice versa. They also discover the role of magnets in particle accelerators and the fundamental principles of electrical circuits.

**Source:** `text_pages/0004_education.fnal.gov_program_stem-outreach` — https://education.fnal.gov/program/stem-outreach  ·  *grounding 0.85*

### 207. Why was Anna Grassellino considered a suitable candidate to chair the quantum subcommittee of the DOE Office of Science Advisory Committee?

Anna Grassellino was considered suitable due to her combination of scientific excellence, technical vision, and leadership in large-scale quantum initiatives. She is an internationally recognized physicist and director of the DOE’s Superconducting Quantum Materials and Systems Center, with a strong background in advancing superconducting technologies for quantum systems.

**Source:** `text_pages/0010_news.fnal.gov_2026_05_anna-grassellino-appointed-to-doe` — https://news.fnal.gov/2026/05/anna-grassellino-appointed-to-doe-office-of-science-advisory-committee  ·  *grounding 0.85*

### 208. What is the function of smaller surrogate models within the Genesis Mission project's AI framework?

Smaller surrogate models in the Genesis Mission project act as rapid stand-ins for more complex and time-consuming design models. They quickly make predictions about crucial chip performance metrics, such as operational speed, power consumption, and transistor performance. These models can evaluate millions of design options within minutes, predicting their performance and isolating the most promising candidates.

**Source:** `text_pages/0008_news.fnal.gov_2026_05_fermilab-leads-multi-lab-ai-initi` — https://news.fnal.gov/2026/05/fermilab-leads-multi-lab-ai-initiative-to-accelerate-design-of-chips-used-in-extreme-environments  ·  *grounding 0.84*

### 209. What is the main challenge in building physics models for transistor behavior at cryogenic temperatures, and how is AI helping to address it?

The main challenge is the time commitment; using standard industry tools, building a robust set of cryogenic physics models for one type of transistor can take around two years, which is slower than the pace of technological advancement. Through the Genesis Mission, AI and machine learning are being utilized to dramatically accelerate these laborious, data-rich research processes.

**Source:** `text_pages/0029_news.fnal.gov_2026_05_using-ai-fermilab-researcher-prob` — https://news.fnal.gov/2026/05/using-ai-fermilab-researcher-probes-how-transistors-behave-in-extreme-cold  ·  *grounding 0.84*

### 210. What is the primary purpose of the MAGIS-100 experiment at Fermilab?

The MAGIS-100 experiment aims to construct a quantum sensing device capable of detecting extremely faint signals emanating from the farthest reaches of the universe. Its goal is to discover new physics phenomena.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.84*

### 211. What is the purpose of the Master of Science in Physics program specializing in quantum science and technology offered by Fermilab and Northern Illinois University?

The purpose of this innovative graduate program is to prepare the next generation of quantum experts. It combines the expertise of a DOE national laboratory quantum center and a prominent state university to achieve this goal.

**Source:** `text_pages/0012_news.fnal.gov_category_newsroom_press-release` — https://news.fnal.gov/category/newsroom/press-release  ·  *grounding 0.84*

### 212. What is the primary objective of the Genesis Mission?

The Genesis Mission is a sweeping U.S. Department of Energy artificial intelligence initiative. Its main objective is to accelerate the design and development of a new class of chips for use in quantum, fusion, and high-radiation environments, achieving a speed and scale not previously seen.

**Source:** `text_pages/0008_news.fnal.gov_2026_05_fermilab-leads-multi-lab-ai-initi` — https://news.fnal.gov/2026/05/fermilab-leads-multi-lab-ai-initiative-to-accelerate-design-of-chips-used-in-extreme-environments  ·  *grounding 0.84*

### 213. What is the primary purpose of the scalable superconducting cavity array being built by Fermilab scientist Yao Lu?

The primary purpose of the scalable superconducting cavity array, being built by Fermilab scientist Yao Lu, is to detect faint signals from mysterious dark photons. This system aims to achieve unprecedented speed and sensitivity in the search for dark matter by harnessing quantum entanglement.

**Source:** `text_pages/0029_news.fnal.gov_tag_dark-matter` — https://news.fnal.gov/tag/dark-matter  ·  *grounding 0.84*

### 214. Why does Fermilab choose not to pre-moderate comments on its official social media accounts?

Fermilab chooses not to pre-moderate comments because it values different opinions and aims to encourage conversation in its online presence. This means users' comments are published automatically without prior review.

**Source:** `text_pages/0008_news.fnal.gov_newsroom_social-media` — https://news.fnal.gov/newsroom/social-media  ·  *grounding 0.83*

### 215. What is the primary goal of the SuperCDMS experiment?

The SuperCDMS experiment is a direct-detection experiment designed to look for signals caused by dark matter particles themselves. It is specifically sensitive to "light dark matter," which refers to dark matter particles with a mass comparable to that of a proton.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.83*

### 216. How does the integration of Fermilab's QICK system with the QASMTrans framework benefit quantum compilation?

The integration of Fermilab's QICK quantum control system with the QASMTrans quantum compilation framework helps bridge the gap between logical circuits and the underlying hardware. This linkage speeds up quantum compilation by 100x, contributing to bringing practical quantum computers closer to reality.

**Source:** `text_pages/0010_news.fnal.gov_tag_qick` — https://news.fnal.gov/tag/qick  ·  *grounding 0.83*

### 217. How do the Fermilab-hosted Saturday Morning Quantum program and the joint Fermilab and Northern Illinois University quantum science program differ in their target audience and educational level?

The Saturday Morning Quantum program, hosted by Fermilab, targets high school students, allowing them to engage directly with lab quantum scientists and engineers. In contrast, the joint program between Fermilab and Northern Illinois University is a Master of Science in Physics program, designed for graduate students specializing in quantum science and technology to prepare future experts.

**Source:** `text_pages/0012_news.fnal.gov_category_newsroom_press-release` — https://news.fnal.gov/category/newsroom/press-release  ·  *grounding 0.83*

### 218. What is the purpose of the collaboration between Fermilab's QICK and Harmoniqs' Piccolo.jl software?

The purpose of the collaboration is to integrate Piccolo.jl, a quantum control and calibration package from Harmoniqs, with QICK. This integration aims to enable more precise and repeatable qubit manipulation, ultimately providing better results in less time.

**Source:** `text_pages/0012_news.fnal.gov_tag_quantum` — https://news.fnal.gov/tag/quantum  ·  *grounding 0.83*

### 219. What educational programs and centers are highlighted by fact sheets at Fermilab?

Fermilab provides fact sheets on educational efforts like Saturday Morning Physics and the VALOR Program, which is an internship. Additionally, it highlights centers such as the Helen Edwards Engineering Research Center and the Illinois Accelerator Research Center (IARC).

**Source:** `text_pages/0019_news.fnal.gov_fact-sheets` — https://news.fnal.gov/fact-sheets  ·  *grounding 0.83*

### 220. How do the direct applications of the LCLS superconducting linac and the SRF systems developed for xLight differ?

The LCLS superconducting linac is described as the world's most powerful X-ray free-electron laser, indicating its direct application in advanced scientific research. In contrast, the SRF systems developed for xLight are intended for semiconductor lithography systems, with the goal of improving semiconductor chips for various modern technologies and defense.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.82*

### 221. How does the core focus of Fermilab as a laboratory compare to the mission of its Education and Public Engagement department?

Fermilab as a laboratory is primarily focused on particle physics and accelerator research, exploring the fundamental nature of the universe. In contrast, its Education and Public Engagement department's mission is to share this science, technology, art, and environmental stewardship with the public to enhance understanding and appreciation of Fermilab's work and the natural world.

**Source:** `text_pages/0003_education.fnal.gov_about` — https://education.fnal.gov/about  ·  *grounding 0.81*

### 222. What is the primary benefit of flux tuning for the new quantum detector in the search for dark matter?

The primary benefit of flux tuning for the new quantum detector is its ability to speed up the search for a tiny signal across a broad range of frequencies. It enables rapid frequency scanning, allowing scientists to use fewer detectors to cover a wide spectrum of possibilities.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 0.81*

### 223. What is quantum coherence, as described by Fang Zhao, in the context of these quantum sensors?

According to Fang Zhao, quantum coherence is a fundamental requirement for quantum devices. It refers to the protection of these devices from external factors like heat or noise, which could obscure fragile signals. Preserving coherence allows these signals to last long enough for detection, ensuring the precision of the sensors.

**Source:** `text_pages/0014_news.fnal.gov_2026_04_new-electronically-tunable-quantu` — https://news.fnal.gov/2026/04/new-electronically-tunable-quantum-detector-speeds-up-search-for-dark-matter  ·  *grounding 0.81*

### 224. What transition does the milestone event for the DUNE experiment represent in its development?

The milestone event for the DUNE experiment represents an important transition from the construction phase to the detector installation phase. It signifies the shift from building the foundational structures to assembling the actual particle detection elements.

**Source:** `text_pages/0009_news.fnal.gov_2026_05_fermilab-marks-major-milestone-fo` — https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment  ·  *grounding 0.80*

### 225. Why is Anna Grassellino's appointment to the DOE Office of Science Advisory Committee significant for national quantum goals?

Anna Grassellino's appointment is significant because she will serve on the SCAC and, more importantly, chair the quantum subcommittee. This subcommittee is specifically tasked with advancing national quantum goals.

**Source:** `text_pages/0012_news.fnal.gov_tag_quantum` — https://news.fnal.gov/tag/quantum  ·  *grounding 0.80*

### 226. What broad aspects of Fermilab are covered by the fact sheets provided in the gallery?

The gallery of fact sheets covers various aspects of Fermilab, including its research activities, the team involved, environmental initiatives, and educational efforts.

**Source:** `text_pages/0019_news.fnal.gov_fact-sheets` — https://news.fnal.gov/fact-sheets  ·  *grounding 0.80*

### 227. Why is Fermilab involved in an AI initiative related to the Genesis Mission?

Fermilab is involved in an AI initiative for the Genesis Mission to accelerate the design of custom computer chips. These chips are specifically intended for use in extreme environments characterized by extreme temperatures, high radiation, and ultra-fast conditions.

**Source:** `text_pages/0016_news.fnal.gov_newsroom_news` — https://news.fnal.gov/newsroom/news  ·  *grounding 0.76*

### 228. What is the main purpose of Fermilab's STEM outreach programs?

Fermilab's STEM outreach programs are designed to highlight Fermilab science to the public. They achieve this by offering hands-on activities, exciting demonstrations, or by connecting participants with staff experts from the lab. These programs are particularly suited for school fairs and STEM-focused community events.

**Source:** `text_pages/0004_education.fnal.gov_program_stem-outreach` — https://education.fnal.gov/program/stem-outreach  ·  *grounding 0.76*

### 229. What scientific topics does Fermilab offer under its "Science for Classrooms" initiative?

Under its "Science for Classrooms" initiative, Fermilab offers topics including Neutrinos, Quantum science, Cosmology, Muons and other fundamental particles, Ecology and the environment, and Scoring Particles.

**Source:** `text_pages/0002_education.fnal.gov` — https://education.fnal.gov  ·  *grounding 0.75*

### 230. How does the SuperCDMS experiment plan to confirm a dark matter detection if a signal is observed?

If the SuperCDMS experiment makes a detection, it will ideally confirm this signal by comparing it with results from other dark matter experiments. An example of such an experiment is LUX-ZEPLIN.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.75*

### 231. Why is the interference pattern created by an interferometer, like the one for MAGIS-100, important for its function as a detector?

The interference pattern created by an interferometer is extremely sensitive to its environment. This sensitivity allows the instrument to be used as a detector, enabling MAGIS-100 to detect dark matter and other phenomena that require very sensitive detection.

**Source:** `text_pages/0008_education.fnal.gov_lederman-science-center` — https://education.fnal.gov/lederman-science-center  ·  *grounding 0.74*

### 232. What is "cooldown" in the context of the SuperCDMS experiment?

In the SuperCDMS experiment, "cooldown" refers to the test of the cryogenic system. This process ensures the system can reach its ultimate target temperature of 20 millikelvin, which is necessary for the experiment's operation.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.73*

### 233. What is Jacopo Bernardini's role within the Proton Improvement Plan-II (PIP-II) project at Fermilab?

Jacopo Bernardini serves as the level-3 manager for the 650-MHz cryomodules for the Proton Improvement Plan-II (PIP-II) project at Fermilab. He joined Fermilab in 2020 and finds satisfaction in collaborating with colleagues worldwide and observing designs become reality.

**Source:** `text_pages/0007_news.fnal.gov_2026_04_largest-neutrino-experiment-in-th` — https://news.fnal.gov/2026/04/largest-neutrino-experiment-in-the-us-wins-project-of-the-year-award  ·  *grounding 0.73*

### 234. Why is the SuperCDMS experiment's cryogenic system considered "unforgiving technology"?

The SuperCDMS experiment's cryogenic system is called "unforgiving technology" because if any part of it does not work correctly, the system will fail to reach its crucial target temperature of 20 millikelvin. Reaching this extremely low temperature is essential for the experiment's function.

**Source:** `text_pages/0009_news.fnal.gov_2026_03_a-chilling-new-search-for-dark-ma` — https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway  ·  *grounding 0.72*

### 235. How do the educational focuses of Fermilab's Subatomic Particles kit and Neutrino Physics kit differ?

The Subatomic Particles kit focuses on the unique and unexpected behavior of subatomic particles in general, covering concepts like particle entanglement and quantum superposition. In contrast, the Neutrino Physics kit specifically explores the mysterious behavior and properties of neutrinos, including their production, detection, and oscillation to change type.

**Source:** `text_pages/0004_education.fnal.gov_program_stem-outreach` — https://education.fnal.gov/program/stem-outreach  ·  *grounding 0.71*

### 236. How does the LCLS-II X-ray laser compare to its predecessor in terms of X-ray flash rate?

The LCLS-II X-ray laser is significantly more powerful, capable of producing up to a million X-ray flashes per second. This represents an 8,000-fold increase compared to its predecessor.

**Source:** `text_pages/0011_news.fnal.gov_2026_04_fermilab-completes-its-part-in-up` — https://news.fnal.gov/2026/04/fermilab-completes-its-part-in-upgrading-worlds-most-powerful-x-ray-laser  ·  *grounding 0.71*

### 237. Why will the Dark Energy Spectroscopic Instrument (DESI) continue its observations beyond its originally planned five-year mission?

The Dark Energy Spectroscopic Instrument (DESI) will continue observations into 2028 for two main reasons. First, the instrument has demonstrated excellent performance. Second, there are hints suggesting that dark energy might evolve, prompting further exploration and expansion of its 3D map of the universe.

**Source:** `text_pages/0012_news.fnal.gov_category_newsroom_press-release` — https://news.fnal.gov/category/newsroom/press-release  ·  *grounding 0.68*

### 238. What activities were mentioned as part of the field trip experience at Fermilab?

The field trip mentioned included visits to three habitats and hunting for bugs. Participants also noted that the docents were very knowledgeable and great with kids.

**Source:** `text_pages/0002_education.fnal.gov` — https://education.fnal.gov  ·  *grounding 0.67*

### 239. Which specific particles are investigated by the Muon g-2 Experiment and the Mu2e Experiment at Fermilab?

Both the Muon g-2 Experiment and the Mu2e Experiment at Fermilab are dedicated to investigating muons.

**Source:** `text_pages/0019_news.fnal.gov_fact-sheets` — https://news.fnal.gov/fact-sheets  ·  *grounding 0.67*

### 240. What are the main objectives of the MUonE experiment at CERN?

The MUonE experiment at CERN has two main objectives. It aims to search for dark matter particles. Additionally, it plans to study the muon's magnetic moment.

**Source:** `text_pages/0029_news.fnal.gov_tag_dark-matter` — https://news.fnal.gov/tag/dark-matter  ·  *grounding 0.64*

### 241. How does the subscription process for Fermilab's internal newsletter differ from the public Fermilab Frontiers newsletter?

The internal newsletter requires subscribers to be Fermilab ID badge holders, such as employees and users, and necessitates authentication. In contrast, the public Fermilab Frontiers newsletter does not mention these specific requirements, implying it is open to a broader audience without a badge or authentication.

**Source:** `text_pages/0007_news.fnal.gov_newsroom_subscribe-to-fermilab-frontiers` — https://news.fnal.gov/newsroom/subscribe-to-fermilab-frontiers  ·  *grounding 0.52*
