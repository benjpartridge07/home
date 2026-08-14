// Shared data for Science Hotshot and its topic selector page.
// SCIENCE_TOPICS lists every topic per subject (matching biology.html / chemistry.html /
// physics.html), so the selector page can show "not built yet" topics as disabled.
// SCIENCE_QUESTIONS tags each question with a topic id (t) so the quiz can be filtered.

const SCIENCE_TOPICS = [
  // Biology
  { id: "bio_cells1", subject: "bio", label: "Animal & Plant Cells", status: "done" },
  { id: "bio_cells2", subject: "bio", label: "Eukaryotes, Prokaryotes & the Scale of Cells", status: "done" },
  { id: "bio_cells3", subject: "bio", label: "Cells: Structure, Transport & Division", status: "done" },
  { id: "bio_cells4", subject: "bio", label: "Cell Specialisation", status: "done" },
  { id: "bio_body1", subject: "bio", label: "Human Body Systems, Part 1: Breathing & Transport", status: "done" },
  { id: "bio_body2", subject: "bio", label: "Human Body Systems, Part 2: Digestion & Control", status: "done" },
  { id: "bio_plants1", subject: "bio", label: "Plants, Part 1: Structure & Transpiration", status: "upcoming" },
  { id: "bio_plants2", subject: "bio", label: "Plants, Part 2: Photosynthesis", status: "upcoming" },
  { id: "bio_health1", subject: "bio", label: "Lifestyle & Health, Part 1: Disease Risk", status: "upcoming" },
  { id: "bio_health2", subject: "bio", label: "Lifestyle & Health, Part 2: Hormones", status: "upcoming" },
  { id: "bio_disease1", subject: "bio", label: "Disease, Part 1: Infection & Defence", status: "upcoming" },
  { id: "bio_disease2", subject: "bio", label: "Disease, Part 2: Treatment & Technology", status: "upcoming" },
  { id: "bio_eco1", subject: "bio", label: "Ecosystems, Part 1: Communities & Fieldwork", status: "upcoming" },
  { id: "bio_eco2", subject: "bio", label: "Ecosystems, Part 2: Biodiversity & Human Impact", status: "upcoming" },
  { id: "bio_inherit", subject: "bio", label: "Inheritance", status: "upcoming" },
  { id: "bio_evolution", subject: "bio", label: "Variation & Evolution", status: "upcoming" },

  // Chemistry — no topics built yet on chemistry.html, so this is a single
  // general-foundations pseudo-topic rather than a real built lesson.
  { id: "chem_general", subject: "chem", label: "General KS3/GCSE Foundations (not yet a full topic)", status: "done" },

  // Physics
  { id: "phys_waves", subject: "phys", label: "Waves", status: "done" },
  { id: "phys_density", subject: "phys", label: "Density & Rearranging Equations", status: "done" },
  { id: "phys_atomic", subject: "phys", label: "Atomic Structure", status: "done" },
  { id: "phys_speed", subject: "phys", label: "Speed, Distance & Acceleration", status: "done" },
];

const SCIENCE_QUESTIONS = [
  // Biology — Animal & Plant Cells
  { s: "bio", t: "bio_cells1", q: "What is the function of the nucleus in a cell?", a: "It contains the genetic material (DNA) and controls the cell's activities." },
  { s: "bio", t: "bio_cells1", q: "Name two structures found in a plant cell but NOT in an animal cell.", a: "Cell wall and chloroplasts (a permanent vacuole also counts)." },
  { s: "bio", t: "bio_cells1", q: "What is the function of mitochondria?", a: "They are the site of (aerobic) respiration, releasing energy for the cell." },

  // Biology — Eukaryotes, Prokaryotes & the Scale of Cells
  { s: "bio", t: "bio_cells2", q: "What is the main difference between a eukaryotic cell and a prokaryotic cell?", a: "Eukaryotic cells have a nucleus and membrane-bound organelles; prokaryotic cells don't — their DNA is free in the cytoplasm." },
  { s: "bio", t: "bio_cells2", q: "Give an example of a prokaryotic organism.", a: "A bacterium." },
  { s: "bio", t: "bio_cells2", q: "Roughly how much bigger is a eukaryotic cell than a bacterial cell?", a: "About 10 times bigger (eukaryotic cells are roughly 10-100 micrometres, bacteria around 1 micrometre)." },

  // Biology — Cells: Structure, Transport & Division
  { s: "bio", t: "bio_cells3", q: "What process do cells use to divide and produce new body cells for growth and repair?", a: "Mitosis." },
  { s: "bio", t: "bio_cells3", q: "What is diffusion?", a: "The net movement of particles from an area of higher concentration to an area of lower concentration." },
  { s: "bio", t: "bio_cells3", q: "What is the name for the movement of water across a partially permeable membrane?", a: "Osmosis." },

  // Biology — Cell Specialisation
  { s: "bio", t: "bio_cells4", q: "What does it mean for a cell to be 'specialised'?", a: "It has differentiated (changed) to have a structure suited to its particular job." },
  { s: "bio", t: "bio_cells4", q: "Give an example of a specialised cell and describe how its structure suits its function.", a: "E.g. a red blood cell — it's a biconcave disc with no nucleus, giving it a large surface area to carry oxygen efficiently." },

  // Biology — Human Body Systems, Part 1: Breathing & Transport
  { s: "bio", t: "bio_body1", q: "What is the function of the alveoli in the lungs?", a: "They provide a large surface area for gas exchange between air and blood (oxygen in, carbon dioxide out)." },
  { s: "bio", t: "bio_body1", q: "Name two features that make the alveoli efficient for gas exchange.", a: "Large surface area, thin walls (one cell thick), good blood supply, and a moist lining (any two)." },
  { s: "bio", t: "bio_body1", q: "What is the function of red blood cells?", a: "To carry oxygen around the body, using haemoglobin." },
  { s: "bio", t: "bio_body1", q: "What are the four chambers of the heart called?", a: "Left atrium, right atrium, left ventricle, right ventricle." },

  // Biology — Human Body Systems, Part 2: Digestion & Control
  { s: "bio", t: "bio_body2", q: "What does the digestive enzyme amylase do?", a: "It breaks down starch into sugars (maltose/glucose)." },
  { s: "bio", t: "bio_body2", q: "Where is bile produced, and what is its job?", a: "Produced in the liver (stored in the gall bladder); it emulsifies fats and neutralises stomach acid to help enzymes digest food." },
  { s: "bio", t: "bio_body2", q: "What is the main role of the small intestine?", a: "It absorbs digested food (nutrients) into the blood." },
  { s: "bio", t: "bio_body2", q: "Which hormone controls blood glucose by letting cells take up glucose?", a: "Insulin." },
  { s: "bio", t: "bio_body2", q: "Which gland produces insulin?", a: "The pancreas." },

  // Chemistry — General KS3/GCSE Foundations
  { s: "chem", t: "chem_general", q: "What are the three states of matter?", a: "Solid, liquid, and gas." },
  { s: "chem", t: "chem_general", q: "What happens to the particles in a solid as it's heated until it melts?", a: "They gain energy and vibrate more, until they have enough energy to break free of fixed positions and move past each other — becoming a liquid." },
  { s: "chem", t: "chem_general", q: "What is an element?", a: "A substance made of only one type of atom." },
  { s: "chem", t: "chem_general", q: "What is a compound?", a: "A substance made of two or more different elements chemically bonded together." },
  { s: "chem", t: "chem_general", q: "What is a mixture?", a: "Two or more substances combined together but not chemically bonded, so they can be separated by physical methods." },
  { s: "chem", t: "chem_general", q: "Which separation method would you use to separate an insoluble solid from a liquid?", a: "Filtration." },
  { s: "chem", t: "chem_general", q: "Which separation method would you use to get a soluble solid back out of a solution?", a: "Evaporation (or crystallisation)." },
  { s: "chem", t: "chem_general", q: "What are the rows in the periodic table called?", a: "Periods." },
  { s: "chem", t: "chem_general", q: "What are the columns in the periodic table called?", a: "Groups." },
  { s: "chem", t: "chem_general", q: "Whereabouts on the periodic table are most metals found?", a: "On the left and in the middle of the table (non-metals are on the right)." },
  { s: "chem", t: "chem_general", q: "What is the name given to the Group 0 elements?", a: "The noble gases." },
  { s: "chem", t: "chem_general", q: "Are noble gases reactive or unreactive, and why?", a: "Unreactive (inert) — they already have a full outer shell of electrons." },
  { s: "chem", t: "chem_general", q: "What is the name given to the Group 1 elements?", a: "The alkali metals." },
  { s: "chem", t: "chem_general", q: "What happens to reactivity as you go down Group 1?", a: "Reactivity increases." },
  { s: "chem", t: "chem_general", q: "What is the smallest part of an element that can still exist?", a: "An atom." },

  // Physics — Waves
  { s: "phys", t: "phys_waves", q: "What is the equation linking wave speed, frequency and wavelength?", a: "Wave speed = frequency × wavelength (v = fλ)." },
  { s: "phys", t: "phys_waves", q: "What is frequency measured in?", a: "Hertz (Hz)." },
  { s: "phys", t: "phys_waves", q: "What's the difference between a transverse wave and a longitudinal wave?", a: "In transverse waves the vibrations are at right angles to the direction of energy transfer; in longitudinal waves they're parallel to it." },
  { s: "phys", t: "phys_waves", q: "Give an example of a longitudinal wave.", a: "Sound waves (or the compressions in a slinky spring)." },

  // Physics — Density & Rearranging Equations
  { s: "phys", t: "phys_density", q: "What is the equation for density?", a: "Density = mass ÷ volume (ρ = m/V)." },
  { s: "phys", t: "phys_density", q: "What are the units of density?", a: "kg/m³ (or g/cm³)." },
  { s: "phys", t: "phys_density", q: "An object has a mass of 20 kg and a volume of 4 m³. What is its density?", a: "5 kg/m³ (20 ÷ 4)." },

  // Physics — Atomic Structure
  { s: "phys", t: "phys_atomic", q: "What are the three subatomic particles found in an atom?", a: "Protons, neutrons, and electrons." },
  { s: "phys", t: "phys_atomic", q: "Where are protons and neutrons located in an atom?", a: "In the nucleus." },
  { s: "phys", t: "phys_atomic", q: "What is the charge of an electron?", a: "Negative (-1)." },
  { s: "phys", t: "phys_atomic", q: "What does an element's atomic number tell you?", a: "The number of protons (which equals the number of electrons) in an atom." },
  { s: "phys", t: "phys_atomic", q: "What is an isotope?", a: "An atom of the same element with the same number of protons but a different number of neutrons." },

  // Physics — Speed, Distance & Acceleration
  { s: "phys", t: "phys_speed", q: "What is the equation for speed?", a: "Speed = distance ÷ time." },
  { s: "phys", t: "phys_speed", q: "What are the units of speed, if distance is in metres and time is in seconds?", a: "Metres per second (m/s)." },
  { s: "phys", t: "phys_speed", q: "What is acceleration?", a: "The rate of change of velocity — how quickly speed changes." },
  { s: "phys", t: "phys_speed", q: "What is the equation for acceleration?", a: "Acceleration = change in velocity ÷ time taken (a = Δv/t)." },
  { s: "phys", t: "phys_speed", q: "A car travels 100 metres in 20 seconds. What is its average speed?", a: "5 m/s (100 ÷ 20)." },
];
