# -*- coding: utf-8 -*-
"""
Curriculum content for NCERT Class 9 Science Chapter 11: Work, Energy and Simple Machines
20 Comprehensive slides with:
- 16 interactive content slides with 32 in-slide checkpoints (2 per content slide)
- 4 dedicated mastery quiz challenge slides with 40 questions total (10 per slide)
- Complete step-by-step solutions for all quiz questions
- Voiceover narration scripts for Prof. Sophia
"""

slides_data = [
    # Slide 1: Concept of Work & Work Done by Constant Force
    {
        "id": 1,
        "title": "Concept of Work & Work Done by a Constant Force",
        "subtitle": "Scientific Definition, Dot Product W = F·s·cos θ, and the Joule (C-2.5)",
        "content": r"""
<p class="lead-p">In everyday colloquial speech, any physical or mental exertion—such as studying for exams, standing still holding a heavy suitcase, or meditating—is called "hard work". In scientific physics, however, <strong>Work</strong> has a very precise, rigorous definition!</p>

<div class="theory-box">
  <h4>1. Scientific Conditions for Work to be Done</h4>
  <p>In physics, work is said to be done if and only if two fundamental conditions are simultaneously satisfied:</p>
  <ol>
    <li><strong>A force must act on the body:</strong> $F \\neq 0$.</li>
    <li><strong>The body must undergo a displacement:</strong> $s \\neq 0$ along or at an angle to the line of action of the force.</li>
  </ol>
  <p>If a student pushes against a rigid concrete wall with all their might until completely exhausted, but the wall does not move ($s = 0$), in physics <strong>zero work</strong> has been done on the wall!</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Mathematical Formulation of Work</h4>
    <p>Work done by a constant force is the scalar (dot) product of force and displacement vectors:</p>
    <p class="highlight-eq">$$W = \vec{F} \cdot \vec{s} = F \cdot s \cdot \\cos\\theta$$</p>
    <p>Where $F$ is force magnitude, $s$ is displacement magnitude, and $\theta$ is the angle between force and displacement vectors.</p>
  </div>
  <div class="card-item">
    <h4>SI Unit of Work: The Joule (J)</h4>
    <p>Work is a <strong>scalar quantity</strong> (it has magnitude but no direction). Its SI unit is the <strong>Joule (J)</strong>, named after James Prescott Joule:</p>
    <p class="highlight-eq">$$1\text{ J} = 1\text{ N} \times 1\text{ m} = 1\text{ N}\cdot\text{m}$$</p>
    <p><strong>1 Joule (J)</strong> is defined as the work done when a force of $1\text{ N}$ displaces an object by $1\text{ m}$ along the force direction ($1\text{ J} = 10^7\text{ ergs}$).</p>
  </div>
</div>
""",
        "sim_type": "work_vector_pull",
        "voice": "Welcome to the Work, Energy and Simple Machines Master Laboratory! In physics, work has a strict definition: a force must act, and the object must move! Mathematically, work equals force times displacement times cosine theta. Let us experiment with our live vector pulling simulator!",
        "checkpoints": [
            {
                "question": "A porter stands completely still for 30 minutes on a railway platform holding a heavy trunk of mass 40 kg on his head. How much work is done by the porter on the trunk?",
                "options": ["3920 J", "400 J", "0 J", "196 J"],
                "correct": 2,
                "explanation": "Because the porter is standing completely stationary, displacement s = 0. Since W = F · s · cos θ, with s = 0 the work done is strictly 0 Joules, regardless of the effort or time."
            },
            {
                "question": "A force of 15 N pulls a toy cart through a horizontal distance of 4 m along the direction of the force (θ = 0°). What is the work done?",
                "options": ["3.75 J", "60 J", "19 J", "0 J"],
                "correct": 1,
                "explanation": "W = F · s · cos 0° = 15 N × 4 m × 1 = 60 J."
            }
        ]
    },

    # Slide 2: Positive, Zero, and Negative Work
    {
        "id": 2,
        "title": "Positive, Zero, and Negative Work",
        "subtitle": "Directional Angle (θ), Porters, Circular Orbits, & Friction (C-2.5)",
        "content": r"""
<p class="lead-p">Because work depends on the cosine of the angle $\\theta$ between force $\\vec{F}$ and displacement $\\vec{s}$, work can be mathematically <strong>positive</strong>, <strong>zero</strong>, or <strong>negative</strong>.</p>

<div class="theory-box">
  <h4>The Three Regimes of Work</h4>
  <div class="grid-3col">
    <div class="card-item">
      <h5>1. Positive Work ($0^{\\circ} \\le \\theta < 90^{\\circ}$)</h5>
      <p>When force has a component in the direction of displacement. For $\\theta = 0^{\\circ}$, $\\cos 0^{\\circ} = +1 \\implies W = +Fs$. Example: A horse pulling a cart forward, or gravity pulling down on a falling raindrop. <strong>The force adds kinetic energy to the body!</strong></p>
    </div>
    <div class="card-item">
      <h5>2. Zero Work ($\\theta = 90^{\\circ}$ or $s = 0$)</h5>
      <p>When force is perpendicular to displacement ($\\cos 90^{\\circ} = 0 \\implies W = 0$). Examples: A porter carrying luggage walking horizontally ($F_{\\text{gravity}}$ is downward, displacement is horizontal); the Moon orbiting Earth (centripetal force is perpendicular to instantaneous velocity).</p>
    </div>
    <div class="card-item">
      <h5>3. Negative Work ($90^{\\circ} < \\theta \\le 180^{\\circ}$)</h5>
      <p>When force opposes motion. For $\\theta = 180^{\\circ}$, $\\cos 180^{\\circ} = -1 \\implies W = -Fs$. Examples: Friction opposing a skidding car; gravity acting on a ball thrown upward ($F_g$ downward, displacement upward). <strong>The force removes kinetic energy!</strong></p>
    </div>
  </div>
</div>

<div class="theory-box">
  <h4>Classic Conceptual Trap: The Railway Porter</h4>
  <p>When a porter carries a suitcase on his head while walking horizontally at constant speed:</p>
  <ul>
    <li>Work done <strong>by gravity</strong> on suitcase: $W = F_g \\cdot s \\cdot \\cos 90^{\\circ} = 0\\text{ J}$.</li>
    <li>Work done <strong>by the porter's upward normal contact force</strong> on suitcase: $W = N \\cdot s \\cdot \\cos 90^{\\circ} = 0\\text{ J}$.</li>
    <li>Work done by the porter against friction between his shoes and the ground is non-zero, but work done on the luggage vertically is strictly zero!</li>
  </ul>
</div>
""",
        "sim_type": "work_sign_angles",
        "voice": "The sign of work reveals energy transfer! When force points with motion, work is positive and the object speeds up. When force is perpendicular, like gravity on a walking porter or centripetal force on an orbiting satellite, work is exactly zero! When force opposes motion, like contact friction, work is negative and energy is extracted.",
        "checkpoints": [
            {
                "question": "A satellite moves in a circular orbit around Earth under the gravitational pull of the Earth. What is the work done by the gravitational force on the satellite in one complete revolution?",
                "options": [
                    "Positive work proportional to orbital radius",
                    "Zero, because gravitational force is always perpendicular to instantaneous displacement",
                    "Negative work due to gravitational attraction",
                    "Infinite work"
                ],
                "correct": 1,
                "explanation": "In uniform circular motion, the gravitational force acts radially toward the center, perpendicular to the tangential displacement (θ = 90°). Since cos 90° = 0, work done is zero at every instant and throughout the entire revolution."
            },
            {
                "question": "A box of mass 10 kg slides 5 m along a rough horizontal floor against a kinetic frictional force of 20 N. What is the work done by the frictional force?",
                "options": ["+100 J", "-100 J", "-500 J", "0 J"],
                "correct": 1,
                "explanation": "Friction acts directly opposite to the displacement (θ = 180°). W = f · s · cos 180° = 20 N × 5 m × (-1) = -100 J."
            }
        ]
    },

    # Slide 3: Energy and Its Multitude of Forms
    {
        "id": 3,
        "title": "Energy: Forms and Environmental Interconversions",
        "subtitle": "The Capacity to Do Work & Technological Transducers (C-2.5)",
        "content": r"""
<p class="lead-p">The concepts of Work and Energy are intimately bound: <strong>Energy is the capacity of a body to do work</strong>. Any entity that can do work possesses energy, and the amount of work it can perform is the quantitative measure of its energy content.</p>

<div class="theory-box">
  <h4>1. Nature and SI Unit of Energy</h4>
  <ul>
    <li>Energy is a <strong>scalar quantity</strong>.</li>
    <li>SI unit: <strong>Joule (J)</strong>, identical to work! $1\\text{ Joule}$ of work requires the expenditure of $1\\text{ Joule}$ of energy.</li>
    <li>A body possessing energy does work by exerting a force on another body, transferring part or all of its energy to that target.</li>
  </ul>
</div>

<div class="theory-box">
  <h4>2. Major Forms of Energy & Everyday Transducers</h4>
  <div class="grid-2col">
    <div class="card-item">
      <h5>Forms of Energy</h5>
      <ul>
        <li><strong>Mechanical:</strong> Kinetic (motion) + Potential (configuration).</li>
        <li><strong>Thermal / Heat:</strong> Random microscopic kinetic energy of atoms.</li>
        <li><strong>Chemical:</strong> Bond energy in food, fossil fuels, explosives, batteries.</li>
        <li><strong>Electrical:</strong> Energy of flowing or separated charges.</li>
        <li><strong>Radiant / Light:</strong> Electromagnetic wave photon energy.</li>
        <li><strong>Nuclear:</strong> Binding energy of nucleons ($E = mc^2$).</li>
      </ul>
    </div>
    <div class="card-item">
      <h5>Everyday Transducers</h5>
      <ul>
        <li><strong>Solar Cell (Photovoltaic):</strong> Light $\\to$ Electrical.</li>
        <li><strong>Microphone:</strong> Acoustic / Sound $\\to$ Electrical.</li>
        <li><strong>Loudspeaker:</strong> Electrical $\\to$ Acoustic / Sound.</li>
        <li><strong>Electric Motor:</strong> Electrical $\\to$ Mechanical.</li>
        <li><strong>Hydroelectric Dam:</strong> Potential $\\to$ Kinetic $\\to$ Electrical.</li>
        <li><strong>Photosynthesis:</strong> Solar radiant $\\to$ Chemical glucose.</li>
      </ul>
    </div>
  </div>
</div>
""",
        "sim_type": "energy_transducer_chain",
        "voice": "Energy is the fundamental currency of the universe: the capacity to do work. Energy takes countless disguises—mechanical, electrical, chemical, thermal, and radiant. In our interactive energy chain simulator, notice how water stored behind a dam converts gravitational potential energy into spinning turbine kinetic energy, which a generator transforms into electricity for your home!",
        "checkpoints": [
            {
                "question": "What energy transformation occurs in a microphone during an audio recording?",
                "options": [
                    "Electrical energy to sound energy",
                    "Sound (acoustic) energy to electrical energy",
                    "Chemical energy to thermal energy",
                    "Nuclear energy to radiant energy"
                ],
                "correct": 1,
                "explanation": "A microphone senses pressure sound waves vibrating a diaphragm and converts that acoustic/mechanical energy into electrical audio signals."
            },
            {
                "question": "An object has the capacity to perform 250 J of mechanical work on a surrounding system. How much energy does the object possess?",
                "options": ["25 J", "250 J", "2500 J", "0 J"],
                "correct": 1,
                "explanation": "Energy is directly defined as the capacity to do work. An object capable of performing 250 J of work possesses exactly 250 J of energy."
            }
        ]
    },

    # Slide 4: Kinetic Energy (K = 1/2 m v^2)
    {
        "id": 4,
        "title": "Kinetic Energy: The Energy of Motion",
        "subtitle": "Analytical Derivation from Work & Quadratic Velocity Scaling (C-2.5)",
        "content": r"""
<p class="lead-p">A speeding bullet, a rushing river, a flying cricket ball, and blowing wind all share a common attribute: they are in motion, and by virtue of their motion, they can perform work on objects they strike. This is <strong>Kinetic Energy</strong>.</p>

<div class="theory-box">
  <h4>1. Definition of Kinetic Energy ($E_k$ or $K$)</h4>
  <p>The <strong>kinetic energy</strong> of an object is the energy it possesses on account of its motion. It equals the total work done on the object by an accelerating force to bring it from rest to its current velocity.</p>
</div>

<div class="theory-box">
  <h4>2. Mathematical Derivation of $K = \\frac{1}{2}mv^2$</h4>
  <p>Consider an object of mass $m$ initially at rest ($u = 0$). Let a constant unbalanced force $F$ act on it over displacement $s$, accelerating it uniformly at rate $a$ to reach final velocity $v$:</p>
  <ul>
    <li>From the third kinematic equation: $v^2 - u^2 = 2as \\implies v^2 - 0 = 2as \\implies s = \\frac{v^2}{2a}$</li>
    <li>From Newton's Second Law: $F = ma$</li>
    <li>Work done by the force: $W = F \\cdot s = (ma) \\cdot \\left(\\frac{v^2}{2a}\\right)$</li>
    <li>Cancelling acceleration $a$:</li>
  </ul>
  <p class="highlight-eq">$$W = \\frac{1}{2} m v^2$$</p>
  <p>Since the work done on the object from rest equals its acquired kinetic energy:</p>
  <p class="highlight-eq">$$K = \\frac{1}{2} m v^2$$</p>
</div>

<div class="theory-box">
  <h4>3. Critical Consequence: The Quadratic Velocity Trap</h4>
  <p>Notice that kinetic energy scales with the <strong>square of velocity ($K \\propto v^2$)</strong>:</p>
  <ul>
    <li>If speed is <strong>doubled ($2v$)</strong>: $K' = \\frac{1}{2}m(2v)^2 = 4 \\cdot \\left(\\frac{1}{2}mv^2\\right) = 4K$ (Quadrupled!).</li>
    <li>If speed is <strong>tripled ($3v$)</strong>: $K' = 9K$ (Nine-fold increase!).</li>
    <li>This quadratic scaling explains why highway car crashes at $100\\text{ km/h}$ inflict four times the destructive damage of crashes at $50\\text{ km/h}$!</li>
  </ul>
</div>
""",
        "sim_type": "kinetic_energy_scaling",
        "voice": "Kinetic energy equals one half m v squared! Notice the immense power of that squared velocity term. If you double a vehicle's speed, its kinetic energy does not merely double—it quadruples! In our interactive crash simulator, watch how doubling the speed drives a dart four times deeper into the clay target.",
        "checkpoints": [
            {
                "question": "A car of mass 1000 kg travels at a speed of 20 m/s (72 km/h). What is its kinetic energy?",
                "options": ["10,000 J", "20,000 J", "200,000 J (200 kJ)", "400,000 J (400 kJ)"],
                "correct": 2,
                "explanation": "K = ½ m v² = ½ × 1000 kg × (20 m/s)² = 500 × 400 = 200,000 J = 200 kJ."
            },
            {
                "question": "If a sprinter's velocity is tripled, by what factor does their kinetic energy increase?",
                "options": ["3 times", "6 times", "9 times", "27 times"],
                "correct": 2,
                "explanation": "Since K ∝ v², if velocity is multiplied by 3, kinetic energy is multiplied by 3² = 9."
            }
        ]
    },

    # Slide 5: The Work-Energy Theorem
    {
        "id": 5,
        "title": "The Work-Energy Theorem",
        "subtitle": "Connecting Work, Velocity Changes, & Braking Distances (C-2.5, C-8.1)",
        "content": r"""
<p class="lead-p">What happens when work is done on an object that is already moving? The connection between net external work and kinetic energy change is codified by the <strong>Work-Energy Theorem</strong>.</p>

<div class="theory-box">
  <h4>1. Formal Statement of the Work-Energy Theorem</h4>
  <p class="highlight-eq">$$\\text{The net work done on an object by the resultant external force}$$ $$\\text{equals the change in its kinetic energy.}$$</p>
  <p class="highlight-eq">$$W_{\\text{net}} = \\Delta K = K_f - K_i = \\frac{1}{2}mv^2 - \\frac{1}{2}mu^2$$</p>
</div>

<div class="theory-box">
  <h4>2. Analytical Derivation</h4>
  <p>For an object of mass $m$ with initial speed $u$ accelerating under net force $F_{\\text{net}}$ over displacement $s$ to final speed $v$:</p>
  <ul>
    <li>Kinematic relation: $v^2 - u^2 = 2as \\implies s = \\frac{v^2 - u^2}{2a}$</li>
    <li>Work done: $W_{\\text{net}} = F_{\\text{net}} \\cdot s = (ma) \\cdot \\left(\\frac{v^2 - u^2}{2a}\\right) = \\frac{1}{2}mv^2 - \\frac{1}{2}mu^2$</li>
  </ul>
  <p><strong>Physical Interpretation:</strong></p>
  <ul>
    <li>If $W_{\\text{net}} > 0$: Kinetic energy increases ($v > u$, speeding up).</li>
    <li>If $W_{\\text{net}} < 0$: Kinetic energy decreases ($v < u$, slowing down, such as braking).</li>
    <li>If $W_{\\text{net}} = 0$: Kinetic energy is constant ($v = u$, uniform speed).</li>
  </ul>
</div>

<div class="theory-box">
  <h4>3. Automobile Braking Distance Formula</h4>
  <p>To halt a moving vehicle ($v = 0$), the braking force $F_b$ does negative work over braking distance $d$:</p>
  <p class="highlight-eq">$$-F_b \\cdot d = 0 - \\frac{1}{2}mu^2 \\implies d = \\frac{mu^2}{2F_b}$$</p>
  <p>Since braking distance $d \\propto u^2$, doubling car speed <strong>quadruples the braking distance</strong>!</p>
</div>
""",
        "sim_type": "work_energy_braking",
        "voice": "The Work-Energy Theorem is one of the most powerful theorems in classical physics: net work done equals the change in kinetic energy! If brakes apply a constant retarding force, stopping distance scales with the square of speed. This fundamental truth of mechanics explains why speed limits save lives on roadways.",
        "checkpoints": [
            {
                "question": "A 2 kg block moving at 10 m/s is brought to rest by friction. What is the total work done by friction on the block?",
                "options": ["+100 J", "-100 J", "-200 J", "+20 J"],
                "correct": 1,
                "explanation": "By the Work-Energy Theorem: W = ΔK = K_final - K_initial = 0 - ½(2)(10²) = 0 - 100 = -100 J."
            },
            {
                "question": "A vehicle moving at speed v requires a minimum distance d to stop under maximum braking. If the vehicle is traveling at 2v, what distance is needed to stop under identical braking force?",
                "options": ["2d", "3d", "4d", "8d"],
                "correct": 2,
                "explanation": "From d = (m · v²) / (2 F_b), braking distance is directly proportional to v². Doubling velocity multiplies stopping distance by 2² = 4."
            }
        ]
    },

    # Slide 6: Gravitational Potential Energy (U = mgh)
    {
        "id": 6,
        "title": "Gravitational Potential Energy (U = mgh)",
        "subtitle": "Work against Gravity, Elevation, & Path Independence (C-2.5)",
        "content": r"""
<p class="lead-p">When you compress a spring, wind a mechanical clock, or lift a barbell off the floor, work is done against internal elastic or external gravitational forces. This work is not lost; it is stored as <strong>Potential Energy</strong>.</p>

<div class="theory-box">
  <h4>1. Defining Potential Energy ($E_p$ or $U$)</h4>
  <p><strong>Potential energy</strong> is the energy possessed by an object by virtue of its position, elevated height, or physical deformation/configuration.</p>
</div>

<div class="theory-box">
  <h4>2. Derivation of Gravitational Potential Energy ($U = mgh$)</h4>
  <p>To raise an object of mass $m$ to a height $h$ above the ground at constant speed:</p>
  <ul>
    <li>The upward applied force must balance the downward gravitational weight: $F = mg$.</li>
    <li>The vertical upward displacement is $s = h$ (in the direction of applied force, $\\theta = 0^{\\circ}$).</li>
    <li>Work done by the lifting agency: $W = F \\cdot s = (mg) \\cdot h$</li>
  </ul>
  <p class="highlight-eq">$$U = mgh$$</p>
  <p>Where $m$ is mass ($\text{kg}$), $g$ is gravitational acceleration ($\approx 9.8\\text{ m/s}^2$), and $h$ is vertical elevation above the chosen reference ground ($\text{m}$).</p>
</div>

<div class="theory-box">
  <h4>3. Vital Principle: Path Independence</h4>
  <p>Because gravity is a <strong>conservative force</strong>, the work done in lifting a mass depends <strong>solely on the initial and final vertical levels ($h$)</strong>, and is completely independent of the path taken:</p>
  <p class="highlight-eq">$$W_{\\text{vertical}} = W_{\\text{ramp}} = W_{\\text{spiral}} = W_{\\text{stairs}} = mgh$$</p>
  <p>Whether you hoist a crate straight up with a crane or push it up a long, winding ramp, the change in gravitational potential energy is identically $mgh$!</p>
</div>
""",
        "sim_type": "path_independence_ramp",
        "voice": "Gravitational potential energy depends purely on height! When lifting an object of mass m through vertical distance h, the work done against gravity is m times g times h. Crucially, gravity is conservative, so taking a vertical ladder, a zigzag ramp, or winding stairs stores the exact same potential energy mgh!",
        "checkpoints": [
            {
                "question": "A mass of 5 kg is raised to a vertical height of 4 m above the ground (take g = 9.8 m/s²). What is its gravitational potential energy relative to the ground?",
                "options": ["20 J", "49 J", "196 J", "392 J"],
                "correct": 2,
                "explanation": "U = mgh = 5 kg × 9.8 m/s² × 4 m = 196 J."
            },
            {
                "question": "A hiker carrying a 10 kg backpack climbs to a mountain summit 500 m high via a 3000 m long winding path. What is the increase in potential energy of the backpack alone? (g = 9.8 m/s²)",
                "options": ["49,000 J (49 kJ)", "294,000 J (294 kJ)", "150,000 J (150 kJ)", "5,000 J (5 kJ)"],
                "correct": 0,
                "explanation": "Potential energy depends solely on vertical height h = 500 m, not the 3000 m path length: ΔU = mgh = 10 × 9.8 × 500 = 49,000 J = 49 kJ."
            }
        ]
    },

    # Slide 7: Conversion between PE and KE: Free Fall Proof
    {
        "id": 7,
        "title": "Conversion Between PE and KE: Free Fall Proof",
        "subtitle": "Step-by-Step Mathematical Invariance of Total Mechanical Energy (C-2.5)",
        "content": r"""
<p class="lead-p">As an object falls freely under gravity, its potential energy continuously decreases while its speed and kinetic energy rise. Does their sum remain constant? Let us mathematically prove that <strong>Total Mechanical Energy ($E = K + U$)</strong> is strictly conserved at every point!</p>

<div class="theory-box">
  <h4>Analytical Proof for a Dropped Body of Mass $m$ from Height $H$</h4>
  <div class="grid-3col">
    <div class="card-item">
      <h5>Point A (Top, Height $H$)</h5>
      <p>Body is at rest ($u = 0$):</p>
      <ul>
        <li>$K_A = \\frac{1}{2}m(0)^2 = 0$</li>
        <li>$U_A = mgH$</li>
        <li><strong>Total $E_A = 0 + mgH = mgH$</strong></li>
      </ul>
    </div>
    <div class="card-item">
      <h5>Point B (Fallen $x$, Height $H - x$)</h5>
      <p>Using $v_B^2 = 0 + 2gx$:</p>
      <ul>
        <li>$K_B = \\frac{1}{2}m(2gx) = mgx$</li>
        <li>$U_B = mg(H - x)$</li>
        <li><strong>Total $E_B = mgx + mgH - mgx = mgH$</strong></li>
      </ul>
    </div>
    <div class="card-item">
      <h5>Point C (Ground, Height $0$)</h5>
      <p>Using $v_C^2 = 0 + 2gH$:</p>
      <ul>
        <li>$K_C = \\frac{1}{2}m(2gH) = mgH$</li>
        <li>$U_C = mg(0) = 0$</li>
        <li><strong>Total $E_C = mgH + 0 = mgH$</strong></li>
      </ul>
    </div>
  </div>
  <p class="highlight-eq">$$E_A = E_B = E_C = mgH = \\text{Constant}$$</p>
  <p>At every point of the fall: $\\Delta K = -\\Delta U \\implies \\frac{1}{2}mv^2 + mgh = \\text{Constant}$.</p>
</div>
""",
        "sim_type": "free_fall_energy_tower",
        "voice": "Watch the beautiful symmetry of energy conservation! When a ball is dropped from height H, potential energy is at its peak and kinetic energy is zero. As it plunges downward, potential energy transforms seamlessly into kinetic energy. At ground level, all potential energy has converted into kinetic energy—yet the sum at every single millisecond is identically m times g times H!",
        "checkpoints": [
            {
                "question": "An object of mass 2 kg is released from rest from a height of 20 m (g = 10 m/s²). What is its kinetic energy at the exact midpoint of its fall (height 10 m)?",
                "options": ["100 J", "200 J", "300 J", "400 J"],
                "correct": 1,
                "explanation": "Total energy E = mgH = 2 × 10 × 20 = 400 J. At midpoint h = 10 m, potential energy U = mgh = 2 × 10 × 10 = 200 J. Since E = K + U ⟹ K = 400 - 200 = 200 J."
            },
            {
                "question": "With what speed will an object dropped from height h strike the ground in the absence of air resistance?",
                "options": ["v = gh", "v = √(gh)", "v = √(2gh)", "v = 2gh"],
                "correct": 2,
                "explanation": "By conservation of mechanical energy: initial PE = final KE ⟹ mgh = ½ m v² ⟹ v² = 2gh ⟹ v = √(2gh)."
            }
        ]
    },

    # Slide 8: The Universal Law of Conservation of Energy
    {
        "id": 8,
        "title": "The Universal Law of Conservation of Energy",
        "subtitle": "Conservative Systems, Dissipation to Heat, & The Simple Pendulum (C-2.5)",
        "content": r"""
<p class="lead-p">The conservation of mechanical energy observed in free fall is a manifestation of an overarching universal decree: <strong>The Law of Conservation of Energy</strong>.</p>

<div class="theory-box">
  <h4>1. Statement of the Universal Law</h4>
  <p class="highlight-eq">$$\\text{Energy can neither be created nor destroyed; it can only be transformed}$$ $$\\text{from one form into another. The total energy of an isolated universe remains strictly constant.}$$</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Oscillation of a Simple Pendulum</h4>
    <p>A swinging pendulum bob perfectly demonstrates cyclic conservation:</p>
    <ul>
      <li><strong>Extreme Positions (A & B):</strong> The bob momentary stops ($v = 0 \\implies K = 0$). Height is maximum ($h$) $\\implies$ <strong>All energy is Potential ($mgh$)</strong>.</li>
      <li><strong>Mean Center Position (O):</strong> Height is minimum ($h = 0 \\implies U = 0$). Speed is maximum $\\implies$ <strong>All energy is Kinetic ($\\frac{1}{2}mv_{\\text{max}}^2$)</strong>.</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>Why Real Pendulums Eventually Halt</h4>
    <p>In a real room, a pendulum eventually stops swinging. Does this violate energy conservation? <strong>Absolutely not!</strong></p>
    <p>Mechanical energy is gradually converted into <strong>thermal energy (heat) and sound</strong> through air resistance and suspension friction. The total energy (mechanical + thermal + acoustic) remains rigorously conserved!</p>
  </div>
</div>
""",
        "sim_type": "pendulum_energy_exchange",
        "voice": "The Law of Conservation of Energy is nature's inviolable rule: energy cannot be created out of nothing, nor can it be annihilated. Look at our swinging pendulum: at the peak of each arc, all its energy is potential; at the bottom, all is kinetic. If friction is present, the mechanical energy degrades into thermal heat, but the grand total never changes!",
        "checkpoints": [
            {
                "question": "At which point in the oscillation of a simple pendulum is its speed and kinetic energy at their maximum?",
                "options": [
                    "At the extreme left position",
                    "At the extreme right position",
                    "At the central equilibrium (mean) position",
                    "Halfway between mean and extreme"
                ],
                "correct": 2,
                "explanation": "At the mean center position, height h is lowest, so potential energy is minimum. By conservation of energy, kinetic energy and velocity reach their maximum."
            },
            {
                "question": "When a bouncing rubber ball eventually stops on the floor, what happened to its original mechanical energy?",
                "options": [
                    "It was completely destroyed by gravity",
                    "It was transformed into thermal energy (heating the ball and floor) and acoustic sound energy",
                    "It turned into chemical mass",
                    "It was absorbed into the vacuum of space"
                ],
                "correct": 1,
                "explanation": "Energy can never be destroyed. On every bounce, internal molecular hysteresis and surface friction convert mechanical energy into heat and sound until all macro motion ceases."
            }
        ]
    },

    # Slide 9: Power: The Rate of Doing Work
    {
        "id": 9,
        "title": "Power: The Rate of Doing Work",
        "subtitle": "Watts, Kilowatts, Horsepower, & P = F·v Formulation (C-2.5)",
        "content": r"""
<p class="lead-p">Suppose a strong youth and a child both carry identical buckets of water up a flight of stairs. Both perform the exact same work ($mgh$). Yet the youth dashes up in 10 seconds, while the child takes 50 seconds. The physical quantity that distinguishes the speed of energy expenditure is <strong>Power</strong>.</p>

<div class="theory-box">
  <h4>1. Defining Power ($P$)</h4>
  <p><strong>Power</strong> is defined as the <strong>rate of doing work</strong>, or the rate of energy consumption/transfer:</p>
  <p class="highlight-eq">$$P = \\frac{W}{t} = \\frac{\\Delta E}{t}$$</p>
  <p>Where $W$ is work done in time $t$. For steady motion under constant force $F$ at speed $v = \\frac{s}{t}$:</p>
  <p class="highlight-eq">$$P = \\frac{F \\cdot s}{t} = F \\cdot v$$</p>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>SI Unit of Power: The Watt (W)</h4>
    <p>Named after James Watt, developer of the steam engine:</p>
    <p class="highlight-eq">$$1\\text{ Watt} = \\frac{1\\text{ Joule}}{1\\text{ second}} = 1\\text{ J/s}$$</p>
    <p><strong>1 Watt</strong> is the power of an appliance that transfers or expends energy at the rate of $1\\text{ Joule per second}$.</p>
  </div>
  <div class="card-item">
    <h4>Larger & Commercial Units of Power</h4>
    <ul>
      <li><strong>Kilowatt (kW):</strong> $1\\text{ kW} = 1000\\text{ W} = 10^3\\text{ W}$</li>
      <li><strong>Megawatt (MW):</strong> $1\\text{ MW} = 1,000,000\\text{ W} = 10^6\\text{ W}$</li>
      <li><strong>Gigawatt (GW):</strong> $1\\text{ GW} = 10^9\\text{ W}$</li>
      <li><strong>Horsepower (hp):</strong> $1\\text{ hp} = 746\\text{ W} \\approx 0.75\\text{ kW}$ (commonly used for car engines and water pumps).</li>
    </ul>
  </div>
</div>
""",
        "sim_type": "power_stair_climb",
        "voice": "Power measures how fast work is done: work divided by time! Two machines might perform the exact same task, but the machine doing it faster delivers vastly more power. The standard unit is the Watt, which equals one Joule per second. For car engines and irrigation pumps, we also use horsepower, where one horsepower equals 746 Watts.",
        "checkpoints": [
            {
                "question": "An electric crane lifts a concrete slab of mass 500 kg to a vertical height of 20 m in 10 seconds (take g = 10 m/s²). What is the useful power output of the crane?",
                "options": ["1,000 W (1 kW)", "5,000 W (5 kW)", "10,000 W (10 kW)", "50,000 W (50 kW)"],
                "correct": 2,
                "explanation": "Work done W = mgh = 500 × 10 × 20 = 100,000 J. Power P = W / t = 100,000 J / 10 s = 10,000 W = 10 kW."
            },
            {
                "question": "A sports car engine develops a power of 150 kW while cruising at a constant speed of 30 m/s. What forward tractive force is the engine exerting?",
                "options": ["500 N", "5,000 N", "45,000 N", "4,500,000 N"],
                "correct": 1,
                "explanation": "Using P = F · v ⟹ F = P / v = 150,000 W / 30 m/s = 5,000 N."
            }
        ]
    },

    # Slide 10: Commercial Unit of Energy (Kilowatt-Hour)
    {
        "id": 10,
        "title": "Commercial Unit of Energy: The Kilowatt-Hour",
        "subtitle": "Conversion to Joules (3.6 × 10⁶ J) & Electricity Metering (C-2.5)",
        "content": r"""
<p class="lead-p">The Joule is an exceptionally small unit of energy—lifting a medium apple by $1\\text{ metre}$ consumes roughly $1\\text{ Joule}$. For municipal electricity grids supplying millions of homes, measuring in Joules would require astronomically cumbersome numbers. Electricity boards therefore bill consumers in <strong>Kilowatt-hours (kWh)</strong>.</p>

<div class="theory-box">
  <h4>1. Defining the Kilowatt-Hour ($\text{kWh}$)</h4>
  <p><strong>1 Kilowatt-hour</strong> (commonly termed <strong>1 Unit</strong> of electricity) is the electrical energy consumed by an appliance of power rating $1\\text{ kW}$ ($1000\\text{ W}$) running continuously for $1\\text{ hour}$ ($3600\\text{ s}$).</p>
</div>

<div class="theory-box">
  <h4>2. Relationship Between Kilowatt-Hour and Joules</h4>
  <p class="highlight-eq">$$1\\text{ kWh} = 1\\text{ Kilowatt} \\times 1\\text{ Hour}$$</p>
  <p class="highlight-eq">$$1\\text{ kWh} = 1000\\text{ W} \\times 3600\\text{ s} = 1000\\text{ J/s} \\times 3600\\text{ s}$$</p>
  <p class="highlight-eq">$$1\\text{ kWh} = 3,600,000\\text{ Joules} = 3.6 \\times 10^6\\text{ J} = 3.6\\text{ MJ}$$</p>
</div>

<div class="theory-box">
  <h4>3. Household Bill Calculation Formula</h4>
  <p>To calculate energy units consumed by household appliances:</p>
  <p class="highlight-eq">$$\\text{Energy (kWh or Units)} = \\frac{\\text{Power (Watts)} \\times \\text{Hours per day} \\times \\text{Number of days}}{1000}$$</p>
  <p><strong>Example:</strong> An electric iron of $1000\\text{ W}$ used for $2\\text{ hours}$ daily consumes: $\\frac{1000 \\times 2}{1000} = 2\\text{ units}$ per day. Over 30 days at ₹6/unit, cost $= 60 \\times 6 = ₹360$.</p>
</div>
""",
        "sim_type": "electric_meter_bill",
        "voice": "The Joule is too tiny for household electricity bills. Instead, power companies measure energy in kilowatt-hours, commonly called units. One kilowatt-hour equals three point six million Joules! In our interactive electric meter simulator, switch on various appliances to watch the disc spin and calculate monthly electricity costs.",
        "checkpoints": [
            {
                "question": "How many Joules of energy are equivalent to 1 Kilowatt-hour (1 kWh)?",
                "options": ["3,600 J", "36,000 J", "3.6 × 10⁶ J (3.6 MJ)", "3.6 × 10⁹ J"],
                "correct": 2,
                "explanation": "1 kWh = 1000 W × 3600 s = 3,600,000 J = 3.6 × 10⁶ J."
            },
            {
                "question": "A 100 W incandescent light bulb is left on for 10 hours daily. How many units (kWh) of electrical energy does it consume in a 30-day month?",
                "options": ["3 units", "30 units", "300 units", "3000 units"],
                "correct": 1,
                "explanation": "Energy = (100 W × 10 h/day × 30 days) / 1000 = 30,000 / 1000 = 30 kWh (30 units)."
            }
        ]
    },

    # Slide 11: Introduction to Simple Machines & Mechanical Advantage
    {
        "id": 11,
        "title": "Introduction to Simple Machines & Mechanical Advantage",
        "subtitle": "Load, Effort, Velocity Ratio, & Mechanical Advantage (C-2.6)",
        "content": r"""
<p class="lead-p">Throughout history, humans have designed tools to amplify muscle power. A <strong>simple machine</strong> is a device by which an applied effort at one point overcomes a larger resistive load at another point, or changes the direction of effort for operational convenience.</p>

<div class="theory-box">
  <h4>1. Key Parameters of Simple Machines</h4>
  <ul>
    <li><strong>Load ($L$):</strong> The resistive force to be overcome by the machine.</li>
    <li><strong>Effort ($E$):</strong> The external force applied to the machine.</li>
    <li><strong>Displacement of Effort ($d_E$) & Displacement of Load ($d_L$):</strong> The distances moved by effort and load during operation.</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Mechanical Advantage ($\text{MA}$)</h4>
    <p>Ratio of the load to the effort:</p>
    <p class="highlight-eq">$$\\text{MA} = \\frac{\\text{Load}}{\\text{Effort}} = \\frac{L}{E}$$</p>
    <ul>
      <li>$\\text{MA} > 1$: <strong>Force Multiplier</strong> ($E < L$, e.g. crowbar, car jack).</li>
      <li>$\\text{MA} < 1$: <strong>Speed / Distance Multiplier</strong> ($E > L$, but load moves further/faster, e.g. sugar tongs, tweezers, bicycle gears).</li>
      <li>$\\text{MA} = 1$: <strong>Direction Changer</strong> ($E = L$, convenient orientation, e.g. single fixed flag pulley).</li>
    </ul>
  </div>
  <div class="card-item">
    <h4>Velocity Ratio ($\text{VR}$) & Efficiency ($\\eta$)</h4>
    <p><strong>Velocity Ratio:</strong> Ratio of effort displacement to load displacement:</p>
    <p class="highlight-eq">$$\\text{VR} = \\frac{d_E}{d_L}$$</p>
    <p><strong>Mechanical Efficiency ($\\eta$):</strong> Ratio of work output to work input:</p>
    <p class="highlight-eq">$$\\eta = \\frac{\\text{Work Output}}{\\text{Work Input}} = \\frac{L \\cdot d_L}{E \\cdot d_E} = \\frac{\\text{MA}}{\\text{VR}}$$</p>
    <p>For an ideal, frictionless machine: $\\eta = 100\\% \\implies \\text{MA} = \\text{VR}$. In all real machines, friction ensures $\\text{MA} < \\text{VR}$ and $\\eta < 100\\%$.</p>
  </div>
</div>
""",
        "sim_type": "machine_ma_efficiency",
        "voice": "Simple machines do not create energy out of nothing—they trade distance for force! The Mechanical Advantage equals load divided by effort. If MA is greater than one, the machine multiplies your force. The Velocity Ratio is effort distance divided by load distance. In an ideal world without friction, MA equals VR, but real machines always lose a bit of energy to friction.",
        "checkpoints": [
            {
                "question": "A mechanic uses a crowbar to lift a heavy stone slab of weight 600 N by applying an effort of 150 N. What is the Mechanical Advantage (MA) of the crowbar?",
                "options": ["0.25", "2.0", "4.0", "750"],
                "correct": 2,
                "explanation": "MA = Load / Effort = 600 N / 150 N = 4.0."
            },
            {
                "question": "In a real machine with friction, how does the Mechanical Advantage (MA) compare with its Velocity Ratio (VR)?",
                "options": ["MA is always greater than VR", "MA is always strictly equal to VR", "MA is less than VR (Efficiency < 100%)", "MA is always zero"],
                "correct": 2,
                "explanation": "Due to unavoidable friction and weight of moving parts, Work Output < Work Input, meaning Efficiency η = MA / VR < 1. Therefore, MA is always less than VR in real machines."
            }
        ]
    },

    # Slide 12: Levers: Principle of Moments & The Three Classes
    {
        "id": 12,
        "title": "Levers: Principle of Moments & The Three Classes",
        "subtitle": "Class 1, Class 2, and Class 3 Levers (FLE Mnemonic) (C-2.6)",
        "content": r"""
<p class="lead-p">The lever is the most ancient and versatile of all simple machines—a rigid bar pivoting around a fixed support point called the <strong>Fulcrum ($F$)</strong>. Archimedes famously proclaimed: <em>"Give me a place to stand, and I will move the Earth!"</em></p>

<div class="theory-box">
  <h4>1. Principle of the Lever (Principle of Moments)</h4>
  <p>In rotational equilibrium, the clockwise moment of the load equals the anticlockwise moment of the effort:</p>
  <p class="highlight-eq">$$\\text{Load} \\times \\text{Load Arm} = \\text{Effort} \\times \\text{Effort Arm}$$</p>
  <p class="highlight-eq">$$\\text{MA} = \\frac{\\text{Load}}{\\text{Effort}} = \\frac{\\text{Effort Arm}}{\\text{Load Arm}}$$</p>
</div>

<div class="theory-box">
  <h4>2. Classification of Levers (The FLE Rule)</h4>
  <p>The three classes depend on which component sits in the <strong>middle</strong>:</p>
  <div class="grid-3col">
    <div class="card-item">
      <h5>Class 1: Fulcrum in Middle (F)</h5>
      <p>Examples: Seesaw, scissors, crowbar, pliers.</p>
      <ul>
        <li>Effort arm can be $>$, $=$, or $<$ load arm.</li>
        <li>$\\text{MA}$ can be $> 1$, $= 1$, or $< 1$.</li>
        <li>Inverts the direction of force!</li>
      </ul>
    </div>
    <div class="card-item">
      <h5>Class 2: Load in Middle (L)</h5>
      <p>Examples: Wheelbarrow, nutcracker, bottle opener.</p>
      <ul>
        <li>Effort arm is <strong>always longer</strong> than load arm.</li>
        <li><strong>Always $\\text{MA} > 1$</strong>.</li>
        <li>Always acts as a <strong>force multiplier</strong>!</li>
      </ul>
    </div>
    <div class="card-item">
      <h5>Class 3: Effort in Middle (E)</h5>
      <p>Examples: Tweezers, tongs, fishing rod, human forearm.</p>
      <ul>
        <li>Load arm is <strong>always longer</strong> than effort arm.</li>
        <li><strong>Always $\\text{MA} < 1$</strong>.</li>
        <li>Acts as a <strong>speed / distance multiplier</strong>!</li>
      </ul>
    </div>
  </div>
</div>
""",
        "sim_type": "lever_three_classes",
        "voice": "Remember the golden mnemonic FLE: 1, 2, 3! In Class 1 levers, the Fulcrum is in the middle, like a seesaw. In Class 2, the Load is in the middle, like a wheelbarrow—MA is always greater than one, giving you pure muscle multiplication. In Class 3, Effort is in the middle, like tweezers or your own forearm—MA is less than one, but your fingertips move with incredible speed and dexterity!",
        "checkpoints": [
            {
                "question": "A nutcracker has its pivot at one end, the nut placed in the center, and the hand pressing the handles at the opposite end. What class of lever is it?",
                "options": ["Class 1", "Class 2", "Class 3", "Class 4"],
                "correct": 1,
                "explanation": "Because the load (the nut) is positioned between the fulcrum and the effort, it is a Class 2 lever (Load in the middle)."
            },
            {
                "question": "In a Class 1 crowbar, the effort arm is 120 cm long and the load arm is 20 cm long. Assuming ideal conditions, what is its Mechanical Advantage?",
                "options": ["0.167", "6.0", "140", "2400"],
                "correct": 1,
                "explanation": "MA = Effort Arm / Load Arm = 120 cm / 20 cm = 6.0."
            }
        ]
    },

    # Slide 13: The Inclined Plane as a Simple Machine
    {
        "id": 13,
        "title": "The Inclined Plane as a Simple Machine",
        "subtitle": "Ramps, Slopes, Screws, and MA = L / h (C-2.6)",
        "content": r"""
<p class="lead-p">Lifting an 80-tonne stone slab vertically into the air is impossible for human laborers. Yet ancient civilizations routinely raised such megaliths atop towering temples. How? By using the simplest machine of all: the <strong>Inclined Plane</strong>.</p>

<div class="theory-box">
  <h4>1. How the Inclined Plane Multiplies Force</h4>
  <p>An inclined plane is a flat, rigid surface tilted at an angle $\\theta$ to the horizontal. Instead of lifting a load $L = mg$ vertically through height $h$, you push it along the ramp length $L_{\\text{ramp}}$:</p>
  <ul>
    <li>The inclined plane's surface provides a normal reaction force ($N = mg \\cos\\theta$) supporting part of the object's weight.</li>
    <li>The required pulling effort along a smooth incline is only the component parallel to the slope: $E = mg \\sin\\theta$.</li>
  </ul>
</div>

<div class="grid-2col">
  <div class="card-item">
    <h4>Mechanical Advantage Formulation</h4>
    <p>For an ideal frictionless inclined plane:</p>
    <p class="highlight-eq">$$\\text{MA} = \\frac{\\text{Load}}{\\text{Effort}} = \\frac{mg}{mg \\sin\\theta} = \\frac{1}{\\sin\\theta}$$</p>
    <p>Since $\\sin\\theta = \\frac{\\text{Height } (h)}{\\text{Length of Incline } (L_{\\text{ramp}})}$:</p>
    <p class="highlight-eq">$$\\text{MA} = \\frac{L_{\\text{ramp}}}{h}$$</p>
    <p>The gentler the slope (longer $L_{\\text{ramp}}$ for the same height $h$), the <strong>greater the Mechanical Advantage</strong>, requiring less pushing effort!</p>
  </div>
  <div class="card-item">
    <h4>Variations of the Inclined Plane</h4>
    <ul>
      <li><strong>Wedge:</strong> Two back-to-back inclined planes used to split wood, chisel rock, or cut (knives, axes, nail tips).</li>
      <li><strong>Screw:</strong> An inclined plane wound helically around a central cylinder. Turning the screw advances the threads with tremendous force amplification.</li>
      <li><strong>Switchback Mountain Roads:</strong> Winding roads increase travel distance to reduce the gradient, allowing heavy trucks to climb mountains.</li>
    </ul>
  </div>
</div>
""",
        "sim_type": "inclined_plane_ramp",
        "voice": "The inclined plane trades distance for force! To lift a barrel onto a truck bed, lifting it vertically takes immense effort. Pushing it up a gentle ramp takes a fraction of that effort over a longer distance. The mechanical advantage equals the ramp length divided by its vertical height: MA equals L over h!",
        "checkpoints": [
            {
                "question": "A ramp of length 6 m is used to roll a heavy drum into a truck bed that is 1.5 m above the ground. Assuming negligible friction, what is the Mechanical Advantage of this ramp?",
                "options": ["0.25", "4.0", "7.5", "9.0"],
                "correct": 1,
                "explanation": "MA = Length of ramp / Vertical height = L / h = 6 m / 1.5 m = 4.0."
            },
            {
                "question": "Why are mountain roads constructed with winding zigzag paths (switchbacks) rather than straight up the steep slope?",
                "options": [
                    "To decrease the total travel distance",
                    "To increase the incline length, reducing slope angle and multiplying mechanical advantage",
                    "To increase gravitational pull on vehicles",
                    "To eliminate friction entirely"
                ],
                "correct": 1,
                "explanation": "Winding switchbacks increase the length of the incline (L_ramp) for the same vertical gain (h), significantly lowering the required engine traction force through a higher Mechanical Advantage."
            }
        ]
    },

    # Slide 14: Pulley Systems: Fixed, Movable, and Block & Tackle
    {
        "id": 14,
        "title": "Pulley Systems: Fixed, Movable, and Block & Tackle",
        "subtitle": "Tension Sharing, Direction Inversion, and MA = n (C-2.6)",
        "content": r"""
<p class="lead-p">A <strong>pulley</strong> is a grooved wheel rotating freely around an axle mounted on a frame (block), designed to guide a rope, cable, or chain. By combining fixed and movable pulleys into a <strong>block and tackle</strong>, heavy industrial loads are hoisted with ease.</p>

<div class="theory-box">
  <h4>1. Three Foundational Pulley Configurations</h4>
  <div class="grid-3col">
    <div class="card-item">
      <h5>Single Fixed Pulley</h5>
      <p>Axle anchored to a ceiling support:</p>
      <ul>
        <li>$d_E = d_L \\implies \\text{VR} = 1$</li>
        <li>$\\text{Ideal MA} = 1$</li>
        <li><strong>Does not multiply force!</strong> Its sole purpose is to change effort direction to downward, allowing a worker to pull down using their body weight.</li>
      </ul>
    </div>
    <div class="card-item">
      <h5>Single Movable Pulley</h5>
      <p>One rope end fixed; load hangs from axle:</p>
      <ul>
        <li>Load is supported by 2 rope strands.</li>
        <li>$2T = L \\implies T = L/2$</li>
        <li>$\\text{Ideal MA} = 2$, $\\text{VR} = 2$</li>
        <li><strong>Acts as a force multiplier:</strong> halves the required effort!</li>
      </ul>
    </div>
    <div class="card-item">
      <h5>Block and Tackle ($n$ Pulleys)</h5>
      <p>Combination of fixed and movable blocks:</p>
      <ul>
        <li>Load is shared across $n$ supporting strands.</li>
        <li>$nT = L \\implies \\text{Effort } E = \\frac{L}{n}$</li>
        <li><strong>$\\text{Ideal MA} = n$, $\\text{VR} = n$</strong></li>
        <li>Effort is divided by the total number of pulley wheels $n$!</li>
      </ul>
    </div>
  </div>
</div>

<div class="theory-box">
  <h4>2. Efficiency in Real Multi-Pulley Systems</h4>
  <p>In a real block and tackle with $n$ pulleys:</p>
  <ul>
    <li>The lower movable pulley block has non-zero mass $w$ that must also be lifted: $E = \\frac{L + w}{n}$.</li>
    <li>Axle friction further reduces mechanical efficiency: $\\eta = \\frac{\\text{MA}}{\\text{VR}} < 100\\%$.</li>
  </ul>
</div>
""",
        "sim_type": "pulley_rig_system",
        "voice": "Pulleys are marvels of mechanical tension! A single fixed pulley does not multiply force—its MA is one—but it allows you to pull downward with your body weight. A single movable pulley splits the load between two rope strands, doubling your force! In a block and tackle system with n pulleys, your lifting power is multiplied n times!",
        "checkpoints": [
            {
                "question": "What is the primary mechanical benefit of using a single fixed pulley, given that its Mechanical Advantage is only 1?",
                "options": [
                    "It cuts the required effort force by half",
                    "It changes the direction of the applied effort to downward, allowing the user to utilize their body weight",
                    "It eliminates rope friction entirely",
                    "It increases the velocity of the load"
                ],
                "correct": 1,
                "explanation": "A single fixed pulley does not multiply force (MA = 1), but conveniently redirects the effort downward, allowing workers to pull down rather than awkwardly hoisting upward."
            },
            {
                "question": "A block and tackle system consists of 4 pulleys (2 fixed and 2 movable). An effort of 150 N is required to lift a load of 480 N. What is the efficiency of this system?",
                "options": ["60%", "75%", "80%", "100%"],
                "correct": 2,
                "explanation": "Velocity ratio VR = n = 4. Mechanical advantage MA = Load / Effort = 480 / 150 = 3.2. Efficiency η = (MA / VR) × 100% = (3.2 / 4) × 100% = 80%."
            }
        ]
    },

    # Slide 15: Kinematics-Dynamics Problem-Solving Workshop
    {
        "id": 15,
        "title": "Comprehensive Problem-Solving Workshop",
        "subtitle": "Water Pumps, Multi-Force Work, & Real Machine Efficiency (C-8.1)",
        "content": r"""
<p class="lead-p">Mastery of work, power, and simple machines requires integrating mass-density relations, kinematic theorems, and practical electrical efficiency.</p>

<div class="theory-box">
  <h4>1. Agricultural Borewell Pump Problem</h4>
  <p><strong>Problem:</strong> An electric motor pumps $1200\\text{ litres}$ of water per minute from a borewell of depth $30\\text{ m}$. Calculate the minimum power rating of the pump in kilowatts (take $g = 9.8\\text{ m/s}^2$ and density of water $= 1\\text{ kg/litre}$).</p>
  <ul>
    <li>Mass of water per minute: $m = 1200\\text{ litres} \\times 1\\text{ kg/litre} = 1200\\text{ kg}$</li>
    <li>Time duration: $t = 1\\text{ minute} = 60\\text{ seconds}$</li>
    <li>Work done lifting water: $W = mgh = 1200\\text{ kg} \\times 9.8\\text{ m/s}^2 \\times 30\\text{ m} = 352,800\\text{ J}$</li>
    <li>Power: $P = \\frac{W}{t} = \\frac{352,800\\text{ J}}{60\\text{ s}} = 5880\\text{ W} = 5.88\\text{ kW}$</li>
    <li>In horsepower: $P = \\frac{5880}{746} \\approx 7.88\\text{ hp}$</li>
  </ul>
</div>

<div class="theory-box">
  <h4>2. Machine Efficiency & Frictional Loss</h4>
  <p>A machine with $\\text{VR} = 5$ requires an effort of $200\\text{ N}$ to lift a load of $800\\text{ N}$ through $2\\text{ m}$:</p>
  <ul>
    <li>$\\text{MA} = \\frac{L}{E} = \\frac{800}{200} = 4.0$</li>
    <li>Efficiency: $\\eta = \\frac{\\text{MA}}{\\text{VR}} \\times 100\\% = \\frac{4.0}{5.0} \\times 100\\% = 80\\%$</li>
    <li>Work Input: $W_{\\text{in}} = E \\cdot d_E = 200\\text{ N} \\times (5 \\times 2\\text{ m}) = 2000\\text{ J}$</li>
    <li>Useful Work Output: $W_{\\text{out}} = L \\cdot d_L = 800\\text{ N} \\times 2\\text{ m} = 1600\\text{ J}$</li>
    <li>Energy lost to friction: $W_{\\text{friction}} = W_{\\text{in}} - W_{\\text{out}} = 2000 - 1600 = 400\\text{ J}$</li>
  </ul>
</div>
""",
        "sim_type": "borewell_pump_calc",
        "voice": "Let us solve real-world engineering problems! When an agricultural pump lifts water from an underground borewell, the power required equals the mass of water lifted per second times g times the depth. If the motor is eighty percent efficient, twenty percent of the incoming electrical energy is dissipated as heat and sound.",
        "checkpoints": [
            {
                "question": "A pump motor lifts 600 kg of water through a vertical height of 20 m in 20 seconds (g = 10 m/s²). What is the output power of the pump?",
                "options": ["600 W", "3,000 W", "6,000 W (6 kW)", "12,000 W"],
                "correct": 2,
                "explanation": "W = mgh = 600 × 10 × 20 = 120,000 J. Power P = W / t = 120,000 J / 20 s = 6,000 W = 6 kW."
            },
            {
                "question": "An ideal machine has a Velocity Ratio of 6. How much effort is required to lift a load of 1800 N?",
                "options": ["300 N", "600 N", "10,800 N", "150 N"],
                "correct": 0,
                "explanation": "For an ideal machine, MA = VR = 6. MA = Load / Effort ⟹ Effort = Load / MA = 1800 N / 6 = 300 N."
            }
        ]
    },

    # Slide 16: Indian Heritage in Machines & Scientific Frontiers
    {
        "id": 16,
        "title": "Indian Heritage in Machines & Modern Frontiers",
        "subtitle": "Megalithic Temple Earth Ramps, Yantras, & Thermodynamic Limits (C-8.1)",
        "content": r"""
<p class="lead-p">Civil engineering in ancient India showcased ingenious applications of simple machines, moving monumental masses without fossil fuels or steam engines.</p>

<div class="theory-box">
  <h4>1. Ancient Indian Mechanical Ingenuity</h4>
  <ul>
    <li><strong>Thanjavur Brihadeeswarar Temple (~1010 CE):</strong> Built by Chola emperor Rajaraja I, the temple tower is crowned by an <strong>80-tonne monolithic granite dome (Kumbam)</strong> at a height of 66 meters. Historical records suggest engineers constructed an inclined earthen ramp over $6\\text{ km}$ long, using elephants, rolling logs, and levers to roll the 80-tonne block to the summit!</li>
    <li><strong>Kautilya's Arthashastra (~300 BCE):</strong> Documents precise classifications of mechanical devices termed <strong>Yantras</strong>, water-lifting levers (*Tula-yantra*), and pulley mechanisms.</li>
    <li><strong>Stepwells of Gujarat and Rajasthan:</strong> Intricate multi-tier water lifting architectures employing specialized pulleys, counterweights, and Archimedean principles.</li>
  </ul>
</div>

<div class="theory-box">
  <h4>2. Modern Scientific Frontiers: Thermodynamic Limits</h4>
  <div class="grid-2col">
    <div>
      <h5>Impossibility of Perpetual Motion Machines</h5>
      <p>Inventors throughout history attempted to design "Perpetual Motion Machines" that do continuous work without energy input. The <strong>First Law of Thermodynamics</strong> (Conservation of Energy) and <strong>Second Law</strong> (Entropy generation) strictly forbid such machines: efficiency $\\eta$ can never exceed $100\\%$!</p>
    </div>
    <div>
      <h5>Global Renewable Energy Transitions</h5>
      <p>Modern power engineering focuses on harvesting diffuse natural energy fluxes: multi-megawatt wind turbines, utility-scale photovoltaic solar parks, and fusion tokamak reactors ($Q > 1$) aiming to replicate solar nuclear fusion on Earth.</p>
    </div>
  </div>
</div>
""",
        "sim_type": "thanjavur_ramp_sim",
        "voice": "Our journey concludes with an awe-inspiring historical marvel: a thousand years ago, Chola engineers in Tamil Nadu hoisted an eighty-tonne solid granite capstone atop the Brihadeeswarar Temple by using a six-kilometer earthen inclined plane! In modern physics, we also recognize nature's ultimate boundary: no machine can ever be more than one hundred percent efficient, ruling out perpetual motion machines forever.",
        "checkpoints": [
            {
                "question": "How did ancient Chola engineers hoist the 80-tonne granite dome (Kumbam) to the 66-meter summit of the Brihadeeswarar Temple in Thanjavur?",
                "options": [
                    "Using steam-powered cranes",
                    "By constructing a gradual, 6-kilometer long inclined earthen ramp",
                    "By dropping it from a hot-air balloon",
                    "Using chemical rocket boosters"
                ],
                "correct": 1,
                "explanation": "Chola engineers utilized a massive inclined earthen ramp over 6 km long with a gentle slope, drastically multiplying mechanical advantage so elephants and rollers could haul the 80-tonne granite monolith to the top."
            },
            {
                "question": "Why is a Perpetual Motion Machine of the First Kind (a machine that outputs continuous useful work with zero energy input) physically impossible?",
                "options": [
                    "Because of patent law restrictions",
                    "It directly violates the First Law of Thermodynamics (Conservation of Energy)",
                    "Because materials cannot withstand high speeds",
                    "Because gravity stops working after 1 hour"
                ],
                "correct": 1,
                "explanation": "A machine creating work without an equivalent input of energy violates the First Law of Thermodynamics (Universal Conservation of Energy), which states that energy cannot be created from nothing."
            }
        ]
    },

    # Slide 17: Quiz Challenge I: Work & Energy Foundations (Q1-10)
    {
        "id": 17,
        "title": "Mastery Quiz Challenge I: Work & Energy Foundations",
        "subtitle": "Questions 1–10 • Comprehensive Diagnostic with Step-by-Step Solutions",
        "content": "<p class=\"lead-p\">Test your mastery of scientific work definitions, $W = F s \\cos\\theta$, positive, zero, and negative work conditions, energy forms, and kinetic energy derivations. Click 'View Solution' for complete mathematical workings.</p>",
        "sim_type": "quiz_slide",
        "voice": "Welcome to Quiz Challenge One! These ten questions test your grasp of work definitions, directional angles, and kinetic energy fundamentals. Think carefully through each problem before checking the solution modal.",
        "quiz_range": (1, 10)
    },

    # Slide 18: Quiz Challenge II: Work-Energy Theorem & Conservation (Q11-20)
    {
        "id": 18,
        "title": "Mastery Quiz Challenge II: Conservation & Free Fall",
        "subtitle": "Questions 11–20 • Quantitative Calculations with Step-by-Step Solutions",
        "content": "<p class=\"lead-p\">Evaluate your skills on the Work-Energy Theorem ($W_{\\text{net}} = \\Delta K$), gravitational potential energy ($U = mgh$), free fall energy invariance, and stopping distance quadratic proportionality. Click 'View Solution' for detailed step-by-step steps.</p>",
        "sim_type": "quiz_slide",
        "voice": "Welcome to Quiz Challenge Two! Here we focus on the Work-Energy Theorem, gravitational potential energy, and mechanical energy conservation during free fall. Work out the numbers step by step!",
        "quiz_range": (11, 20)
    },

    # Slide 19: Quiz Challenge III: Power & Electrical Units (Q21-30)
    {
        "id": 19,
        "title": "Mastery Quiz Challenge III: Power & Electricity Billing",
        "subtitle": "Questions 21–30 • Watts, Kilowatts, Kilowatt-Hours, & Appliance Costs",
        "content": "<p class=\"lead-p\">Assess your conceptual and numerical mastery of power ($P = W/t = Fv$), SI units (Watts), horsepower conversion ($1\\text{ hp} = 746\\text{ W}$), and household energy billing in kilowatt-hours ($3.6\\times 10^6\\text{ J}$). Inspect each solution popup for clear explanations.</p>",
        "sim_type": "quiz_slide",
        "voice": "Quiz Challenge Three examines power and commercial kilowatt-hours. Remember that power is the rate of energy expenditure, while kilowatt-hour is a unit of total energy!",
        "quiz_range": (21, 30)
    },

    # Slide 20: Quiz Challenge IV: Simple Machines & Frontiers (Q31-40)
    {
        "id": 20,
        "title": "Mastery Quiz Challenge IV: Simple Machines & Frontiers",
        "subtitle": "Questions 31–40 • Levers, Inclined Planes, Pulleys, & Ancient Megaliths",
        "content": "<p class=\"lead-p\">The final test of your mechanics mastery! Tackle Mechanical Advantage, Velocity Ratio, Efficiency, Lever Classes (1, 2, 3), Inclined Planes, and Pulley rigs. Click 'View Solution' for complete derivations.</p>",
        "sim_type": "quiz_slide",
        "voice": "You have reached the final mastery challenge of Chapter 11! These ten multi-step engineering questions cover levers, inclined planes, pulleys, and thermodynamic limits. Excellent work reaching the end of Work, Energy and Simple Machines!",
        "quiz_range": (31, 40)
    }
]

# 40 Rigorous Quiz Questions
quiz_questions = [
    # Q1
    {
        "num": 1,
        "question": "A force of 20 N acts on an object displacing it horizontally by 5 m in the direction of the force. How much work is done?",
        "options": ["4 J", "25 J", "100 J", "200 J"],
        "correct": 2,
        "solution": "Step 1: Formula for work done: W = F · s · cos θ.\nStep 2: Since displacement is in the direction of the force, θ = 0° and cos 0° = 1.\nStep 3: W = 20 N × 5 m × 1 = 100 J."
    },
    # Q2
    {
        "num": 2,
        "question": "In which of the following scenarios is the work done by the specified force strictly ZERO?",
        "options": [
            "A person lifting a bucket vertically from a well",
            "A satellite orbiting Earth in a circular orbit acted upon by gravitational force",
            "A car braking to a stop on a road",
            "A stretched bow accelerating an arrow"
        ],
        "correct": 1,
        "solution": "Step 1: In circular motion, gravitational force is directed toward the center of the orbit.\nStep 2: The instantaneous displacement is tangential to the circle.\nStep 3: The angle between force and displacement is θ = 90°. Since cos 90° = 0, W = F · s · cos 90° = 0 J."
    },
    # Q3
    {
        "num": 3,
        "question": "A ball of mass 0.5 kg thrown vertically upward reaches a peak height of 10 m (g = 9.8 m/s²). What is the work done by gravity during the ascent?",
        "options": ["+49 J", "-49 J", "0 J", "+98 J"],
        "correct": 1,
        "solution": "Step 1: Downward gravitational force: F_g = mg = 0.5 × 9.8 = 4.9 N.\nStep 2: Upward displacement: s = 10 m.\nStep 3: Gravity acts downward while displacement is upward, so θ = 180°.\nStep 4: W = F · s · cos 180° = 4.9 × 10 × (-1) = -49 J."
    },
    # Q4
    {
        "num": 4,
        "question": "A body of mass 4 kg has a linear momentum of 24 kg·m/s. What is its kinetic energy?",
        "options": ["36 J", "72 J", "144 J", "288 J"],
        "correct": 1,
        "solution": "Step 1: Relationship between kinetic energy K and momentum p: K = p² / (2m).\nStep 2: Substitute values: K = (24)² / (2 × 4) = 576 / 8 = 72 J."
    },
    # Q5
    {
        "num": 5,
        "question": "If both the mass and speed of a moving object are doubled, what happens to its kinetic energy?",
        "options": ["It doubles", "It quadruples", "It increases by 8 times", "It increases by 16 times"],
        "correct": 2,
        "solution": "Step 1: Original kinetic energy: K = ½ m v².\nStep 2: New kinetic energy: K' = ½ (2m) (2v)² = ½ (2m) (4v²) = 8 · [½ m v²] = 8 K.\nConclusion: Kinetic energy increases by a factor of 8."
    },
    # Q6
    {
        "num": 6,
        "question": "An object of mass 10 kg is lifted to a height of 6 m. How much gravitational potential energy does it gain? (Take g = 9.8 m/s²)",
        "options": ["58.8 J", "98 J", "588 J", "1176 J"],
        "correct": 2,
        "solution": "Step 1: Formula for gravitational potential energy: U = mgh.\nStep 2: Substitute values: U = 10 kg × 9.8 m/s² × 6 m = 588 J."
    },
    # Q7
    {
        "num": 7,
        "question": "A force of 5 N acts on a 2 kg block initially at rest for a distance of 8 m. According to the Work-Energy Theorem, what is the final kinetic energy of the block?",
        "options": ["10 J", "20 J", "40 J", "80 J"],
        "correct": 2,
        "solution": "Step 1: By the Work-Energy Theorem, W_net = ΔK = K_final - K_initial.\nStep 2: Initial kinetic energy K_initial = 0 since the block starts from rest.\nStep 3: Work done W = F · s = 5 N × 8 m = 40 J.\nStep 4: Therefore, K_final = 40 J."
    },
    # Q8
    {
        "num": 8,
        "question": "What is the equivalent fundamental SI unit representation of the Joule?",
        "options": ["kg·m/s", "kg·m/s²", "kg·m²/s²", "kg²·m/s²"],
        "correct": 2,
        "solution": "Step 1: 1 Joule = 1 Newton × 1 meter.\nStep 2: Since 1 Newton = 1 kg·m/s², multiplying by meter gives: 1 J = (1 kg·m/s²) × m = 1 kg·m²/s²."
    },
    # Q9
    {
        "num": 9,
        "question": "A pendulum bob has 50 J of potential energy at its highest point of swing. If air resistance is neglected, what is its kinetic energy as it passes through the lowest point?",
        "options": ["0 J", "25 J", "50 J", "100 J"],
        "correct": 2,
        "solution": "Step 1: By the Law of Conservation of Mechanical Energy: Total Energy E = K + U = constant.\nStep 2: At highest point, K = 0 ⟹ E = 50 J.\nStep 3: At lowest point, potential energy U = 0 ⟹ K = E = 50 J."
    },
    # Q10
    {
        "num": 10,
        "question": "A car accelerates from 10 m/s to 20 m/s. The work required to produce this speed increase is:",
        "options": [
            "Equal to the work required to accelerate it from 0 to 10 m/s",
            "Twice the work required to accelerate it from 0 to 10 m/s",
            "Three times the work required to accelerate it from 0 to 10 m/s",
            "Four times the work required to accelerate it from 0 to 10 m/s"
        ],
        "correct": 2,
        "solution": "Step 1: Work from 0 to 10 m/s: W₁ = ½ m (10² - 0²) = ½ m (100) = 50 m.\nStep 2: Work from 10 to 20 m/s: W₂ = ½ m (20² - 10²) = ½ m (400 - 100) = ½ m (300) = 150 m.\nStep 3: Ratio W₂ / W₁ = 150 m / 50 m = 3.\nConclusion: Accelerating from 10 to 20 m/s requires three times as much work."
    },

    # Q11
    {
        "num": 11,
        "question": "A ball of mass 1 kg is dropped from a height of 45 m. Taking g = 10 m/s², what is its velocity just before it strikes the ground?",
        "options": ["15 m/s", "20 m/s", "30 m/s", "45 m/s"],
        "correct": 2,
        "solution": "Step 1: By conservation of energy, initial PE = final KE ⟹ mgh = ½ m v².\nStep 2: Cancel mass m: v² = 2gh ⟹ v = √(2gh).\nStep 3: v = √(2 × 10 × 45) = √900 = 30 m/s."
    },
    # Q12
    {
        "num": 12,
        "question": "A car of mass 1200 kg moving at 25 m/s (90 km/h) applies brakes and halts in 50 m. What is the average braking force?",
        "options": ["3,750 N", "7,500 N", "15,000 N", "30,000 N"],
        "correct": 1,
        "solution": "Step 1: Initial kinetic energy: K_i = ½ m u² = ½ × 1200 × (25)² = 600 × 625 = 375,000 J.\nStep 2: By the Work-Energy Theorem: -F_b · d = 0 - K_i ⟹ F_b × 50 = 375,000.\nStep 3: F_b = 375,000 / 50 = 7,500 N."
    },
    # Q13
    {
        "num": 13,
        "question": "An arrow of mass 0.05 kg is fired from a bow with an initial velocity of 60 m/s. How much potential energy was stored in the stretched bow?",
        "options": ["45 J", "90 J", "180 J", "360 J"],
        "correct": 1,
        "solution": "Step 1: By conservation of energy, the elastic potential energy stored in the bow converts into the kinetic energy of the arrow.\nStep 2: U_elastic = K_arrow = ½ m v² = ½ × 0.05 kg × (60 m/s)² = 0.025 × 3600 = 90 J."
    },
    # Q14
    {
        "num": 14,
        "question": "An electric crane raises a load of 2000 kg through a vertical height of 15 m. How much work is done against gravity? (g = 9.8 m/s²)",
        "options": ["30,000 J", "147,000 J", "294,000 J (294 kJ)", "588,000 J"],
        "correct": 2,
        "solution": "Step 1: Work done against gravity: W = mgh.\nStep 2: W = 2000 kg × 9.8 m/s² × 15 m = 294,000 J = 294 kJ."
    },
    # Q15
    {
        "num": 15,
        "question": "A spring has spring constant k = 200 N/m. How much work is required to compress the spring by 0.1 m from its unstretched length?",
        "options": ["1 J", "2 J", "10 J", "20 J"],
        "correct": 0,
        "solution": "Step 1: Work done compressing a spring equals stored elastic potential energy: W = ½ k x².\nStep 2: W = ½ × 200 N/m × (0.1 m)² = 100 × 0.01 = 1 J."
    },
    # Q16
    {
        "num": 16,
        "question": "A bullet of mass 10 g (0.01 kg) moving at 400 m/s strikes a wooden target and penetrates 0.2 m before stopping. What is the average resistive force exerted by the wood?",
        "options": ["400 N", "2,000 N", "4,000 N", "8,000 N"],
        "correct": 2,
        "solution": "Step 1: Initial kinetic energy K_i = ½ m v² = ½ × 0.01 kg × (400 m/s)² = 0.005 × 160,000 = 800 J.\nStep 2: By the Work-Energy Theorem: -F_avg · d = -K_i ⟹ F_avg × 0.2 = 800.\nStep 3: F_avg = 800 / 0.2 = 4,000 N."
    },
    # Q17
    {
        "num": 17,
        "question": "A stone of mass 2 kg falls freely from a height of 50 m. What is its potential energy after falling for 2 seconds? (Take g = 10 m/s²)",
        "options": ["400 J", "600 J", "800 J", "1000 J"],
        "correct": 1,
        "solution": "Step 1: Distance fallen in 2 seconds: s = ut + ½gt² = 0 + ½(10)(2²) = 5 × 4 = 20 m.\nStep 2: Remaining height above ground: h = 50 m - 20 m = 30 m.\nStep 3: Potential energy at this height: U = mgh = 2 kg × 10 m/s² × 30 m = 600 J."
    },
    # Q18
    {
        "num": 18,
        "question": "Which of the following graphs correctly represents the variation of Gravitational Potential Energy (U) with height (h) above the ground for a given mass?",
        "options": [
            "A horizontal line parallel to the h-axis",
            "A straight line passing through the origin with slope equal to mg",
            "A parabola opening upward",
            "A hyperbola asymptotic to both axes"
        ],
        "correct": 1,
        "solution": "Step 1: The equation for gravitational potential energy is U = mgh.\nStep 2: For constant mass m and gravity g, U is directly proportional to h (U ∝ h).\nStep 3: This represents a linear relation y = mx passing through the origin (0, 0) with slope equal to mg."
    },
    # Q19
    {
        "num": 19,
        "question": "If the kinetic energy of an object is increased by 300% (becoming 4 times its original value), by what percentage does its linear momentum increase?",
        "options": ["50%", "100%", "200%", "300%"],
        "correct": 1,
        "solution": "Step 1: Momentum is related to kinetic energy by p = √(2m · K).\nStep 2: If K' = 4K, then p' = √(2m · 4K) = 2 · √(2m · K) = 2p.\nStep 3: Percentage increase in momentum = [(p' - p) / p] × 100% = [(2p - p) / p] × 100% = 100%."
    },
    # Q20
    {
        "num": 20,
        "question": "A roller coaster car of mass 500 kg starts from rest at the top of a hill of height 35 m. Assuming a frictionless track, what is its speed at the bottom of a 15 m high hill? (g = 10 m/s²)",
        "options": ["10 m/s", "14.1 m/s", "20 m/s", "26.5 m/s"],
        "correct": 2,
        "solution": "Step 1: Loss in potential energy = gain in kinetic energy: mg (h₁ - h₂) = ½ m v².\nStep 2: Cancel mass m: g (35 - 15) = ½ v² ⟹ 10 × 20 = ½ v² ⟹ 200 = ½ v² ⟹ v² = 400.\nStep 3: v = √400 = 20 m/s."
    },

    # Q21
    {
        "num": 21,
        "question": "A machine does 18,000 Joules of work in 2 minutes. What is the power output of the machine?",
        "options": ["150 W", "300 W", "9,000 W", "36,000 W"],
        "correct": 0,
        "solution": "Step 1: Convert time to seconds: t = 2 minutes = 2 × 60 = 120 s.\nStep 2: Power formula: P = W / t.\nStep 3: P = 18,000 J / 120 s = 150 W."
    },
    # Q22
    {
        "num": 22,
        "question": "How many Watts are in one horsepower (1 hp)?",
        "options": ["500 W", "746 W", "1000 W", "1200 W"],
        "correct": 1,
        "solution": "Step 1: By standard imperial-to-SI engineering definition, 1 horsepower (hp) = 746 Watts (approximately 0.746 kW)."
    },
    # Q23
    {
        "num": 23,
        "question": "An electric immersion heater is rated at 1500 W. If it is used for 2 hours daily, how much electrical energy does it consume in 30 days?",
        "options": ["30 kWh", "45 kWh", "90 kWh", "180 kWh"],
        "correct": 2,
        "solution": "Step 1: Daily energy consumption = Power (kW) × Time (h) = 1.5 kW × 2 h = 3.0 kWh.\nStep 2: Total monthly consumption = 3.0 kWh/day × 30 days = 90 kWh (90 units)."
    },
    # Q24
    {
        "num": 24,
        "question": "A girl of mass 40 kg runs up a flight of 30 stairs, each 15 cm high, in 9 seconds. What is her power output? (Take g = 10 m/s²)",
        "options": ["150 W", "200 W", "300 W", "600 W"],
        "correct": 1,
        "solution": "Step 1: Total vertical height: h = 30 stairs × 0.15 m = 4.5 m.\nStep 2: Work done against gravity: W = mgh = 40 kg × 10 m/s² × 4.5 m = 1800 J.\nStep 3: Power output: P = W / t = 1800 J / 9 s = 200 W."
    },
    # Q25
    {
        "num": 25,
        "question": "A motor vehicle moves at a constant speed of 20 m/s against an aerodynamic drag and friction force of 600 N. What engine power is required to maintain this speed?",
        "options": ["30 W", "1,200 W", "6,000 W", "12,000 W (12 kW)"],
        "correct": 3,
        "solution": "Step 1: For steady motion, engine forward force F = resistive force = 600 N.\nStep 2: Power relation: P = F · v.\nStep 3: P = 600 N × 20 m/s = 12,000 W = 12 kW."
    },
    # Q26
    {
        "num": 26,
        "question": "If electricity costs ₹7.00 per unit (kWh), what is the cost of running a 2000 W air conditioner for 8 hours?",
        "options": ["₹16.00", "₹56.00", "₹112.00", "₹224.00"],
        "correct": 2,
        "solution": "Step 1: Energy consumed in kWh = (2000 W × 8 h) / 1000 = 16 kWh (16 units).\nStep 2: Total cost = 16 units × ₹7.00 = ₹112.00."
    },
    # Q27
    {
        "num": 27,
        "question": "Which of the following physical quantities is measured in Kilowatt-hours (kWh)?",
        "options": ["Power", "Force", "Electrical Energy", "Electric Current"],
        "correct": 2,
        "solution": "Step 1: Kilowatt is a unit of power (Energy/time), and hour is a unit of time.\nStep 2: Power × time = Energy.\nConclusion: Kilowatt-hour is a commercial unit of energy, not power."
    },
    # Q28
    {
        "num": 28,
        "question": "Two brothers Alex (mass 50 kg) and Ben (mass 50 kg) climb the same 10 m high rope. Alex reaches the top in 20 s, while Ben takes 40 s. Which statement is correct?",
        "options": [
            "Alex does more work than Ben",
            "Ben does more work than Alex",
            "Both do equal work, but Alex delivers twice the power of Ben",
            "Both deliver equal power"
        ],
        "correct": 2,
        "solution": "Step 1: Work done depends solely on mgh: W = 50 × g × 10, identical for both.\nStep 2: Power P = W / t. Since Alex takes half the time (20 s vs 40 s), his power is double Ben's power: P_Alex = 2 · P_Ben."
    },
    # Q29
    {
        "num": 29,
        "question": "A water pump raises 1000 litres of water (1000 kg) through a height of 18 m in 1 minute. What is the power of the pump? (Take g = 9.8 m/s²)",
        "options": ["294 W", "1,470 W", "2,940 W (2.94 kW)", "5,880 W"],
        "correct": 2,
        "solution": "Step 1: Work done W = mgh = 1000 kg × 9.8 m/s² × 18 m = 176,400 J.\nStep 2: Time t = 1 min = 60 s.\nStep 3: Power P = W / t = 176,400 / 60 = 2,940 W = 2.94 kW."
    },
    # Q30
    {
        "num": 30,
        "question": "A household consumes 250 units of electricity in a month. How much energy is this in Joules?",
        "options": ["9 × 10⁸ J (900 MJ)", "9 × 10⁶ J", "2.5 × 10⁸ J", "3.6 × 10⁶ J"],
        "correct": 0,
        "solution": "Step 1: 1 unit = 1 kWh = 3.6 × 10⁶ J.\nStep 2: 250 units = 250 × 3.6 × 10⁶ J = 900 × 10⁶ J = 9 × 10⁸ J = 900 MJ."
    },

    # Q31
    {
        "num": 31,
        "question": "A lever has an effort arm of 90 cm and a load arm of 15 cm. What is its Mechanical Advantage (MA)?",
        "options": ["0.167", "6.0", "75", "1350"],
        "correct": 1,
        "solution": "Step 1: By the Principle of Moments, MA = Effort Arm / Load Arm.\nStep 2: MA = 90 cm / 15 cm = 6.0."
    },
    # Q32
    {
        "num": 32,
        "question": "Which class of lever always has a Mechanical Advantage strictly GREATER than 1?",
        "options": ["Class 1", "Class 2", "Class 3", "None of the above"],
        "correct": 1,
        "solution": "Step 1: In a Class 2 lever (Load in the middle), the effort arm is always longer than the load arm.\nStep 2: Since MA = Effort Arm / Load Arm, MA is always strictly greater than 1, acting as a force multiplier."
    },
    # Q33
    {
        "num": 33,
        "question": "A wheelbarrow carries a load of 800 N. The distance from the wheel axle (fulcrum) to the load center is 0.5 m, and the distance to the handles (effort) is 1.5 m. What effort force is needed to lift the handles?",
        "options": ["200 N", "266.7 N", "400 N", "2400 N"],
        "correct": 1,
        "solution": "Step 1: Wheelbarrow is a Class 2 lever: Load × Load Arm = Effort × Effort Arm.\nStep 2: 800 N × 0.5 m = Effort × 1.5 m ⟹ 400 = 1.5 × Effort.\nStep 3: Effort = 400 / 1.5 = 266.7 N."
    },
    # Q34
    {
        "num": 34,
        "question": "Why does a pair of sugar tongs or human forearm (Class 3 lever) have a Mechanical Advantage less than 1?",
        "options": [
            "Because it is an imperfect machine with too much friction",
            "Because the effort is in the middle, making the effort arm shorter than the load arm",
            "Because it cannot lift any weight",
            "Because its efficiency is zero"
        ],
        "correct": 1,
        "solution": "Step 1: In Class 3 levers, the effort is applied between the fulcrum and the load.\nStep 2: This geometric arrangement means Effort Arm < Load Arm.\nStep 3: Consequently, MA = Effort Arm / Load Arm < 1. It acts as a speed and displacement multiplier."
    },
    # Q35
    {
        "num": 35,
        "question": "An inclined plane has a length of 10 m and rises to a vertical height of 2 m. What is its ideal Mechanical Advantage?",
        "options": ["0.2", "2.0", "5.0", "20.0"],
        "correct": 2,
        "solution": "Step 1: Formula for ideal Mechanical Advantage of an inclined plane: MA = Length of Incline (L) / Height (h).\nStep 2: MA = 10 m / 2 m = 5.0."
    },
    # Q36
    {
        "num": 36,
        "question": "A block and tackle system has 5 pulleys. An effort of 120 N lifts a load of 450 N. What is the efficiency of the pulley system?",
        "options": ["60%", "75%", "85%", "90%"],
        "correct": 1,
        "solution": "Step 1: Velocity ratio VR = n = 5.\nStep 2: Mechanical Advantage MA = Load / Effort = 450 N / 120 N = 3.75.\nStep 3: Efficiency η = (MA / VR) × 100% = (3.75 / 5) × 100% = 75%."
    },
    # Q37
    {
        "num": 37,
        "question": "A worker uses an inclined plane of efficiency 80% to push a 200 kg barrel up a 5 m long ramp of height 1 m. What effort force along the incline must the worker exert? (g = 10 m/s²)",
        "options": ["400 N", "500 N", "625 N", "1000 N"],
        "correct": 1,
        "solution": "Step 1: Load L = mg = 200 × 10 = 2000 N.\nStep 2: Velocity ratio VR = L_ramp / h = 5 m / 1 m = 5.\nStep 3: Since η = MA / VR ⟹ MA = η × VR = 0.80 × 5 = 4.0.\nStep 4: Effort E = Load / MA = 2000 N / 4.0 = 500 N."
    },
    # Q38
    {
        "num": 38,
        "question": "In Kautilya's ancient Indian treatise 'Arthashastra' (~300 BCE), what general Sanskrit term is used to describe mechanical machines and engineering contrivances?",
        "options": ["Chakra", "Yantra", "Vimana", "Sutra"],
        "correct": 1,
        "solution": "Step 1: In the Arthashastra, Kautilya systematically categorizes mechanical contrivances, waterwheels, and pulley assemblies as 'Yantras' (such as Tula-yantras for levers and balances)."
    },
    # Q39
    {
        "num": 39,
        "question": "Why can NO real machine ever achieve a mechanical efficiency of 100%?",
        "options": [
            "Because of atmospheric air pressure",
            "Because some energy is always converted into non-recoverable thermal and acoustic energy due to friction and moving part mass",
            "Because gravity increases as machines operate",
            "Because Mechanical Advantage must always be an integer"
        ],
        "correct": 1,
        "solution": "Step 1: In all real machines, mechanical parts have inertia/mass and contact surfaces experience friction.\nStep 2: Part of the input work is inevitably dissipated as thermal heat and sound.\nStep 3: By the Second Law of Thermodynamics, Work Output < Work Input, ensuring efficiency η < 100%."
    },
    # Q40
    {
        "num": 40,
        "question": "An electric pump rated at 2 kW of electrical input power has an efficiency of 75%. How much water can it lift from a well 15 m deep in 1 minute? (g = 10 m/s²)",
        "options": ["600 kg (600 litres)", "750 kg", "6,000 kg (6000 litres)", "9,000 kg"],
        "correct": 0,
        "solution": "Step 1: Useful mechanical output power = Input Power × Efficiency = 2000 W × 0.75 = 1500 W.\nStep 2: Useful work done in 1 minute (60 s): W = P_out × t = 1500 W × 60 s = 90,000 J.\nStep 3: Useful work lifting water: W = mgh ⟹ 90,000 = m × 10 × 15 ⟹ 90,000 = 150 m.\nStep 4: Mass of water m = 90,000 / 150 = 600 kg (600 litres)."
    }
]

if __name__ == '__main__':
    assert len(slides_data) == 20, f"Expected 20 slides, got {len(slides_data)}"
    assert len(quiz_questions) == 40, f"Expected 40 quiz questions, got {len(quiz_questions)}"
    for i, q in enumerate(quiz_questions, 1):
        assert q["num"] == i, f"Question number mismatch: {q['num']} != {i}"
        assert len(q["options"]) == 4, f"Question {i} does not have 4 options"
        assert 0 <= q["correct"] <= 3, f"Question {i} invalid correct index"
    print("All 20 slides and 40 quiz questions for Chapter 11 verified successfully!")
