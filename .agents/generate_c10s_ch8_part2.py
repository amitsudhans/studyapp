#!/usr/bin/env python3
"""
Generate Part 2 (Slides 9 to 16) for NCERT Class 10 Science Chapter 8: Heredity.
Strict requirements:
- Short title: strictly 1-3 words.
- Spoken lecture: strictly 195-215 words per slide.
- No persona titles (Dr, Sir, Madam, Mr, Mrs, Prof) and no character names (Raghav, etc.).
- Deeply pedagogical, aligned with NCERT Class 10 Science Chapter 8 syllabus.
"""

import json

SLIDES_PART2 = [
    {
        "id": 9,
        "title": "Dihybrid Cross Assortment",
        "subtitle": "Simultaneous Inheritance of Two Contrasting Traits & Uniform F1 Generation",
        "speech": (
            "To discover how two distinct characters behave when inherited simultaneously, Gregor Mendel conducted a classic dihybrid "
            "breeding experiment in garden pea plants. He selected two pure-breeding parental varieties differing in two observable traits: "
            "seed shape and seed color. One parent possessed round yellow seeds, represented by the homozygous dominant genotype capital R "
            "capital R capital Y capital Y. The contrasting parent possessed wrinkled green seeds, represented by the homozygous recessive "
            "genotype lowercase r lowercase r lowercase y lowercase y. During meiotic gamete formation, the round yellow parent produced "
            "gametes carrying capital R capital Y alleles, while the wrinkled green parent produced gametes carrying lowercase r lowercase y "
            "alleles. When cross-pollination occurred, fertilization united these alleles to generate the first filial generation, known as "
            "the F1 progeny. Every single F1 plant possessed the heterozygous dihybrid genotype capital R lowercase r capital Y lowercase y. "
            "Because round seed shape completely dominates wrinkled seed shape, and yellow seed color completely dominates green seed color, "
            "all F1 plants without exception produced exclusively round yellow seeds. This remarkable uniformity demonstrated that dominant "
            "alleles completely mask recessive alleles in the first generation, even when two separate pairs of contrasting characters are "
            "tracked simultaneously across generations."
        ),
        "objectives": [
            "Define a dihybrid cross tracking two contrasting character pairs simultaneously.",
            "Identify parental genotypes: homozygous round yellow (RRYY) and wrinkled green (rryy).",
            "Explain why the F1 progeny (RrYy) uniformly displays the round yellow phenotype."
        ],
        "key_takeaways": [
            "Dihybrid crosses study the simultaneous inheritance of two pairs of contrasting traits.",
            "Pure-breeding RRYY produces RY gametes; pure-breeding rryy produces ry gametes.",
            "All F1 progeny inherit RrYy and show round yellow seeds due to complete dominance of R and Y."
        ],
        "checkpoints": [
            {
                "question": "What seed phenotype was exhibited by all plants in the F1 generation of Mendel's dihybrid cross?",
                "options": [
                    "Wrinkled green seeds",
                    "Round green seeds",
                    "Round yellow seeds",
                    "Wrinkled yellow seeds"
                ],
                "answer": 2,
                "hint": "Recall which two traits are completely dominant in pea seed shape and color.",
                "explanation": "Round shape (R) dominates wrinkled (r), and yellow color (Y) dominates green (y); thus all F1 (RrYy) plants produce round yellow seeds."
            },
            {
                "question": "What is the genotype of the F1 generation plants in this dihybrid cross?",
                "options": [
                    "RRYY",
                    "rryy",
                    "RrYy",
                    "Rryy"
                ],
                "answer": 2,
                "hint": "Each F1 plant inherits one allele for each trait from each parent.",
                "explanation": "Fusion of an RY gamete from the round yellow parent and an ry gamete from the wrinkled green parent produces the heterozygous genotype RrYy."
            }
        ]
    },
    {
        "id": 10,
        "title": "Independent Assortment Principle",
        "subtitle": "F2 Dihybrid Segregation, The 9:3:3:1 Phenotypic Ratio & Recombinant Traits",
        "speech": (
            "When Mendel allowed the heterozygous F1 plants with round yellow seeds to self-pollinate, the resulting second filial generation "
            "revealed groundbreaking biological insights. Because the gene pair governing seed shape segregates independently from the gene "
            "pair governing seed color, each F1 plant produces four distinct gametic combinations in equal proportions: capital R capital Y, "
            "capital R lowercase y, lowercase r capital Y, and lowercase r lowercase y. Constructing a sixteen-box Punnett square reveals sixteen "
            "genetic fusions yielding four distinct physical phenotypes in the F2 generation. Mendel counted nine plants with round yellow "
            "seeds, three with round green seeds, three with wrinkled yellow seeds, and one with wrinkled green seeds, establishing the classic "
            "nine to three to three to one dihybrid phenotypic ratio. Most importantly, alongside the original parental combinations of round "
            "yellow and wrinkled green, completely new recombinant varieties appeared in substantial numbers: round green and wrinkled yellow. The emergence of these "
            "novel trait mixtures conclusively proved Gregor Mendel's Law of Independent Assortment. This fundamental genetic principle states that "
            "alleles for different traits assort into gametes completely independently of one another during sexual reproduction, creating "
            "abundant diversity among offspring without altering or degrading the underlying hereditary units across generations."
        ),
        "objectives": [
            "Construct the 16-box Punnett square illustrating dihybrid F2 segregation.",
            "Analyze the classic 9:3:3:1 Mendelian phenotypic ratio in the F2 generation.",
            "Explain how recombinant varieties prove the principle of independent assortment."
        ],
        "key_takeaways": [
            "F1 dihybrid plants produce four types of gametes in equal proportions: RY, Ry, rY, and ry.",
            "The F2 generation produces 4 phenotypes in a 9:3:3:1 ratio (9 round yellow, 3 round green, 3 wrinkled yellow, 1 wrinkled green).",
            "New recombinant phenotypes (round green and wrinkled yellow) demonstrate that traits inherit independently."
        ],
        "checkpoints": [
            {
                "question": "What is the classic phenotypic ratio observed in the F2 generation of a Mendelian dihybrid cross?",
                "options": [
                    "3 : 1",
                    "1 : 2 : 1",
                    "9 : 3 : 3 : 1",
                    "1 : 1 : 1 : 1"
                ],
                "answer": 2,
                "hint": "Recall the sixteen-box Punnett square distribution for two independent traits.",
                "explanation": "The F2 generation of a dihybrid cross yields 9 round yellow : 3 round green : 3 wrinkled yellow : 1 wrinkled green, forming a 9:3:3:1 ratio."
            },
            {
                "question": "What critical biological insight does the appearance of round green and wrinkled yellow seeds prove?",
                "options": [
                    "Traits blend irreversibly during gamete fusion",
                    "The genes for seed shape and seed color assort independently into gametes",
                    "Wrinkled seeds cannot undergo sexual reproduction",
                    "Dominant alleles are gradually destroyed over multiple generations"
                ],
                "answer": 1,
                "hint": "Consider why novel trait combinations appear that did not exist in either pure parent.",
                "explanation": "The formation of new trait combinations demonstrates independent assortment: alleles for seed shape separate independently from alleles for seed color."
            }
        ]
    },
    {
        "id": 11,
        "title": "Gene Expression Mechanism",
        "subtitle": "Cellular DNA as Information Source, Coding Sections & Protein Synthesis",
        "speech": (
            "To understand how inherited factors physically produce observable traits, we must examine the molecular machinery inside the "
            "cell nucleus. Cellular deoxyribonucleic acid, commonly abbreviated as DNA, serves as the ultimate master information source "
            "for synthesizing all proteins within an organism. A specific section or segment of DNA that contains the complete biochemical "
            "instructions for synthesizing a particular functional protein is defined as a gene for that protein. Within the living cell, genetic "
            "information flows systematically from DNA sequences to messenger ribonucleic acid molecules, which travel directly to ribosomes to direct "
            "the precise assembly of amino acid chains into functional proteins. Some of these proteins serve as vital structural building blocks "
            "that form cell membranes, muscle fibers, and cellular scaffolds, while others function as specialized catalytic enzymes. These "
            "cellular enzymes accelerate and regulate vital biochemical reactions and metabolic pathways throughout the body. Therefore, an inherited physical characteristic "
            "or visible trait is simply the outward manifestation of specific proteins synthesized according to the instructions encoded in "
            "cellular genes. When an organism inherits a particular gene variant from its parents, its cells produce corresponding proteins "
            "that directly shape its physical structure, physiology, and overall biological capabilities across its lifetime."
        ),
        "objectives": [
            "Explain cellular DNA as the primary information source for protein synthesis.",
            "Define a gene as a specific DNA section coding for a particular functional protein.",
            "Describe how gene-directed protein synthesis leads to the physical expression of traits."
        ],
        "key_takeaways": [
            "Cellular DNA provides the complete informational blueprint for building all cellular proteins.",
            "A gene is a discrete segment of DNA that carries instructions for a specific protein.",
            "Visible physical traits are the direct biochemical outcomes of functional proteins synthesized by cells."
        ],
        "checkpoints": [
            {
                "question": "What is the biological definition of a gene according to molecular genetics?",
                "options": [
                    "A whole chromosome found exclusively in reproductive gametes",
                    "A section of cellular DNA providing instructions for synthesizing a specific protein",
                    "A lipid membrane enclosing the cell nucleus",
                    "A sugar molecule providing immediate energy for cell division"
                ],
                "answer": 1,
                "hint": "Think of the specific segment of DNA that holds the coding instructions for proteins.",
                "explanation": "A gene is a section of DNA that contains the coded instructions required to synthesize a specific functional protein."
            },
            {
                "question": "What biomolecule acts as the master information storehouse for protein synthesis in living cells?",
                "options": [
                    "Cellular DNA (Deoxyribonucleic acid)",
                    "Phospholipid bilayer",
                    "Glycogen polymer",
                    "Adenosine triphosphate"
                ],
                "answer": 0,
                "hint": "Identify the genetic polymer located inside the cell nucleus.",
                "explanation": "Cellular DNA contains the hereditary information and nucleotide sequences required to direct the synthesis of cellular proteins."
            }
        ]
    },
    {
        "id": 12,
        "title": "Enzymes Hormones Control",
        "subtitle": "Enzyme Efficiency, Plant Growth Hormone Biosynthesis & Tall vs Dwarf Expression",
        "speech": (
            "We can see exactly how genes control physical characteristics by examining plant height in garden peas. The height of a plant "
            "is directly governed by the concentration of specific plant growth hormones synthesized in its growing shoots and stems. The "
            "production of this growth hormone is an enzymatic process, catalyzed step by step by a specific cellular enzyme. If the gene "
            "coding for this enzyme functions normally and efficiently, a substantial amount of the active enzyme is produced. This efficient "
            "enzyme synthesizes abundant growth hormone, stimulating rapid cell elongation and causing the pea plant to grow tall and robust. Conversely, "
            "if an alteration or mutation occurs in that gene, the instructions become modified, leading to the synthesis of a less efficient "
            "or partially defective enzyme. Because this altered enzyme works with significantly reduced catalytic efficiency, only a small quantity of plant growth "
            "hormone is produced. Without sufficient growth hormone, cellular elongation remains restricted, and the plant develops as a dwarf. "
            "Thus, Mendelian genes control physical traits like height by regulating the efficiency of specific enzymes, which in turn control "
            "the biosynthesis of key hormones that dictate outward physiological growth, stature, and anatomical form throughout plant life."
        ),
        "objectives": [
            "Explain how plant height depends directly on the quantity of synthesized growth hormone.",
            "Relate hormone synthesis to the catalytic efficiency of gene-encoded cellular enzymes.",
            "Contrast the biochemical mechanisms leading to tall versus dwarf phenotypes."
        ],
        "key_takeaways": [
            "Plant height depends directly on the concentration of growth hormones synthesized in tissues.",
            "Genes direct the synthesis of enzymes that catalyze the production of these growth hormones.",
            "An efficient enzyme yields abundant hormone producing a tall plant; an altered less efficient enzyme causes dwarfism."
        ],
        "checkpoints": [
            {
                "question": "How does a dominant allele 'T' cause a pea plant to grow tall at the biochemical level?",
                "options": [
                    "By blocking water absorption in roots",
                    "By coding for a highly efficient enzyme that synthesizes abundant growth hormone",
                    "By destroying chlorophyll pigments in leaves",
                    "By preventing the plant from undergoing cellular respiration"
                ],
                "answer": 1,
                "hint": "Connect the gene to an active enzyme and the resulting hormone production.",
                "explanation": "The dominant allele produces an efficient enzyme that catalyzes the synthesis of abundant plant growth hormone, resulting in tall plants."
            },
            {
                "question": "What biochemical defect results in the dwarf phenotype in recessive 'tt' pea plants?",
                "options": [
                    "The plant lacks cell walls completely",
                    "An altered gene produces a less efficient enzyme, synthesizing insufficient growth hormone",
                    "The plant produces toxic acids that shrink its stems",
                    "The chloroplasts fail to capture sunlight"
                ],
                "answer": 1,
                "hint": "Consider what happens to enzyme efficiency when the recessive gene instructions are altered.",
                "explanation": "The recessive allele codes for a less efficient enzyme, leading to lower growth hormone production and restricted plant height."
            }
        ]
    },
    {
        "id": 13,
        "title": "Chromosomal Heredity Basis",
        "subtitle": "Paired Chromosomes, Independent Gene Segregation & Meiotic Reduction",
        "speech": (
            "If both parents contribute genetic material equally to their offspring, a critical biological dilemma arises: why does the "
            "total amount of cellular DNA and number of chromosomes not double in each successive generation? The solution lies in the structural "
            "organization of chromosomes and the specialized mechanism of meiotic cell division. Genes are not strung together along a "
            "single continuous DNA thread; instead, they are organized into discrete structural units called chromosomes. In normal body "
            "or somatic cells, chromosomes exist in matched pairs, known as homologous chromosome pairs, creating a diploid condition where "
            "one chromosome of each pair comes from the father and the other from the mother. When an organism produces germ cells or gametes "
            "through meiosis, a specialized reduction division occurs. During meiosis, paired homologous chromosomes separate, ensuring that each resulting "
            "sperm or egg cell receives only a single chromosome from each pair, becoming haploid. When fertilization takes place, the fusion "
            "of two haploid gametes restores the complete diploid number of paired chromosomes and original DNA content in the single-celled zygote. This "
            "precise meiotic segregation ensures species stability across generations while allowing independent assortment of genes located "
            "on different chromosome pairs throughout the biological kingdom."
        ),
        "objectives": [
            "Understand that genes reside on discrete structural chromosomes organized in homologous pairs.",
            "Describe how meiotic reduction division prevents chromosome doubling in sexual reproduction.",
            "Explain how fertilization restores the species-specific diploid chromosome number in the zygote."
        ],
        "key_takeaways": [
            "Genes are organized along discrete structural chromosomes occurring in homologous pairs.",
            "Somatic cells are diploid (paired chromosomes); germ cells are haploid (one chromosome per pair).",
            "Meiosis halves the chromosome count during gametogenesis, and fertilization restores the original diploid number."
        ],
        "checkpoints": [
            {
                "question": "Why does the chromosome number remain constant across generations rather than doubling during sexual reproduction?",
                "options": [
                    "Half the chromosomes dissolve spontaneously in water after fertilization",
                    "Meiotic reduction division halves the chromosome count so each gamete carries only one chromosome from each pair",
                    "Only the maternal parent donates chromosomes to the offspring",
                    "Offspring destroy extra paternal chromosomes upon hatching or birth"
                ],
                "answer": 1,
                "hint": "Recall the specialized cell division that produces haploid gametes.",
                "explanation": "Meiosis reduces the chromosome number by half in germ cells; when gametes fuse during fertilization, the diploid number is restored."
            },
            {
                "question": "What is the chromosomal state of human somatic cells compared to human germ cells (gametes)?",
                "options": [
                    "Somatic cells are haploid; germ cells are diploid",
                    "Somatic cells are diploid with paired chromosomes; germ cells are haploid with single chromosomes",
                    "Both somatic cells and germ cells are triploid",
                    "Somatic cells have no chromosomes; germ cells have all chromosomes"
                ],
                "answer": 1,
                "hint": "Think about pairs versus single representative chromosomes in body cells versus reproductive cells.",
                "explanation": "Body (somatic) cells are diploid, carrying 23 pairs of chromosomes, whereas germ cells are haploid, carrying 23 single chromosomes."
            }
        ]
    },
    {
        "id": 14,
        "title": "Sex Determination Cues",
        "subtitle": "Environmental vs Genetic Mechanisms Across the Animal Kingdom",
        "speech": (
            "The biological mechanisms that determine whether an individual organism develops into a male or a female exhibit remarkable "
            "diversity across the animal kingdom. In some animal species, sex determination is completely non-genetic, governed instead by external "
            "environmental cues experienced during critical early developmental windows. For example, in certain reptiles such as specific turtles, "
            "crocodiles, and lizards, the incubation temperature of fertilized eggs in the nest directly determines the sex of the emerging "
            "hatchlings. In other animals, such as garden snails, individuals are hermaphroditic and can flexibly change their functional sex during "
            "their adult lives, conclusively demonstrating that their sex is not permanently fixed by genetics. Conversely, in humans and most mammals, "
            "sex determination is strictly genetic, established irrevocably at the exact moment of fertilization. An individual's sex in these "
            "species is determined entirely by the specific combination of inherited sex chromosomes received from the paternal and maternal "
            "gametes. Unlike reptiles responding to nest temperatures, external environmental factors like temperature, nutrition, or maternal health "
            "play zero role in deciding whether a human embryo develops into a male or a female, highlighting the diverse evolutionary paths "
            "organisms have taken to regulate sexual reproduction and maintain balanced natural populations."
        ),
        "objectives": [
            "Contrast environmental sex determination with genetic sex determination.",
            "Cite examples of environmental sex determination (reptiles with incubation temperature, snails changing sex).",
            "Establish that human sex determination is strictly genetic and established at fertilization."
        ],
        "key_takeaways": [
            "Sex determination can be environmental (temperature-dependent in reptiles, flexible in snails) or genetic.",
            "In certain reptiles, nest incubation temperature determines offspring sex.",
            "In humans and mammals, sex is determined strictly by inherited sex chromosomes at the moment of fertilization."
        ],
        "checkpoints": [
            {
                "question": "In which of the following organisms does ambient incubation temperature determine the sex of offspring?",
                "options": [
                    "Humans",
                    "Certain reptiles such as turtles and lizards",
                    "Pea plants",
                    "Bacteria"
                ],
                "answer": 1,
                "hint": "Think of cold-blooded animals whose nest warmth influences embryo gender.",
                "explanation": "In certain reptiles like turtles and lizards, the temperature at which fertilized eggs are incubated determines the sex of the offspring."
            },
            {
                "question": "What evidence proves that sex is not genetically fixed in common garden snails?",
                "options": [
                    "They do not possess DNA in their cells",
                    "Individuals can change sex during their lifetime based on mating context",
                    "They only reproduce by budding and spore formation",
                    "All snails are permanently female throughout history"
                ],
                "answer": 1,
                "hint": "Consider the ability of some mollusks to alter their reproductive gender as adults.",
                "explanation": "Snails can change their sex during their lifespan, proving that their sexual identity is not permanently fixed by genetic chromosomes."
            }
        ]
    },
    {
        "id": 15,
        "title": "Human Sex Chromosomes",
        "subtitle": "22 Autosomal Pairs, The Perfect XX Female & The Mismatched XY Male",
        "speech": (
            "Every normal human body cell contains forty-six chromosomes arranged neatly into twenty-three distinct homologous pairs. Twenty-two of "
            "these pairs are known as autosomes. Autosomes carry crucial genes responsible for general bodily design, structural anatomy, and vital cellular metabolic functions, and they "
            "are completely identical in shape, size, and gene loci between human males and females. The twenty-third pair, however, comprises "
            "the specialized sex chromosomes, which differ fundamentally between the two biological sexes. Human females possess two perfectly "
            "matched, normal-sized sex chromosomes designated as capital X capital X. Because both sex chromosomes are completely identical, females are "
            "described as homogametic, and all maternal ova produced through meiosis inevitably carry a single capital X chromosome. Human males, "
            "by contrast, possess a mismatched pair of sex chromosomes designated as capital X capital Y. While the capital X chromosome is "
            "normal-sized, the capital Y chromosome is noticeably shorter, distinctly shaped, and contains specialized male-determining genes. Because males possess "
            "both an X and a Y chromosome, they are termed heterogametic individuals. During natural spermatogenesis, meiotic reduction division segregates this mismatched pair into equal "
            "proportions: fifty percent of sperm carry an X chromosome, while the remaining fifty percent carry a Y chromosome."
        ),
        "objectives": [
            "Distinguish between 22 pairs of autosomes and the single pair of sex chromosomes in humans.",
            "Identify the female sex chromosome constitution as XX (homogametic).",
            "Identify the male sex chromosome constitution as XY (heterogametic, producing 50% X and 50% Y sperm)."
        ],
        "key_takeaways": [
            "Humans possess 23 chromosome pairs: 22 pairs of autosomes and 1 pair of sex chromosomes.",
            "Females possess two matching X chromosomes (XX); males possess one X and one smaller Y chromosome (XY).",
            "All female eggs carry an X chromosome, whereas male sperm are divided equally: 50% carry X and 50% carry Y."
        ],
        "checkpoints": [
            {
                "question": "How many pairs of autosomes are present in normal human body cells?",
                "options": [
                    "23 pairs",
                    "22 pairs",
                    "1 pair",
                    "46 pairs"
                ],
                "answer": 1,
                "hint": "Subtract the single pair of sex chromosomes from the total of 23 pairs.",
                "explanation": "Human somatic cells have 23 pairs of chromosomes in total: 22 pairs are autosomes and 1 pair is sex chromosomes."
            },
            {
                "question": "What is the sex chromosome combination found in normal human biological males?",
                "options": [
                    "XX",
                    "YY",
                    "XY",
                    "XXX"
                ],
                "answer": 2,
                "hint": "Identify the mismatched combination of a normal-sized X and a shorter Y chromosome.",
                "explanation": "Human males have an XY combination, possessing one normal-sized X chromosome and one shorter Y chromosome."
            }
        ]
    },
    {
        "id": 16,
        "title": "Sex Inheritance Probability",
        "subtitle": "Gametic Fusion, The 50-50 Probability Ratio & Paternal Genetic Determination",
        "speech": (
            "Because human mothers possess two X chromosomes, every single egg cell produced by a female inevitably contributes an X chromosome "
            "to the offspring. The genetic sex of the child is therefore determined entirely by which type of sperm cell from the father succeeds "
            "in fertilizing the egg. If an egg cell is fertilized by a sperm carrying an X chromosome, the resulting zygote receives an X from "
            "the mother and an X from the father, establishing the genetic combination XX. This embryo develops normally into a female child. Conversely, if an "
            "egg cell is fertilized by a sperm carrying a Y chromosome, the zygote receives an X from the mother and a Y from the father, "
            "establishing the genetic combination XY. This embryo develops into a male child. Because a human father produces X-bearing sperm and Y-bearing "
            "sperm in exactly equal fifty-fifty proportions, every single pregnancy carries a precise statistical probability of fifty percent "
            "for a girl and fifty percent for a boy. This scientific reality disproves longstanding social prejudices that hold mothers responsible "
            "for the sex of their children. Genetically, the father's fertilizing gamete alone determines the baby's sex with an exact, unbiased "
            "one-to-one mathematical probability across all human societies."
        ),
        "objectives": [
            "Demonstrate using a Punnett square that sex determination in humans follows a strict 50-50 probability ratio.",
            "Explain why the father's fertilizing sperm determines the sex of the offspring.",
            "Dispel societal misconceptions and clarify that mothers do not determine the sex of their children."
        ],
        "key_takeaways": [
            "All children inherit an X chromosome from their mother.",
            "A child inheriting an X chromosome from the father becomes female (XX); inheriting a Y chromosome becomes male (XY).",
            "The father's sperm determines the baby's sex, and the probability of having a boy or a girl is exactly 50% (1:1 ratio) in every pregnancy."
        ],
        "checkpoints": [
            {
                "question": "Which parent genetically determines the sex of the child in humans?",
                "options": [
                    "The mother, because she provides the egg and cellular apparatus",
                    "The father, because his sperm carries either an X or a Y chromosome",
                    "Both parents equally contribute Y chromosomes",
                    "Neither parent; sex is determined by room temperature after delivery"
                ],
                "answer": 1,
                "hint": "Recall which parent produces two different types of gametes (X and Y).",
                "explanation": "Since mothers only contribute X chromosomes, the father's sperm carrying either an X or a Y chromosome determines whether the child will be XX (female) or XY (male)."
            },
            {
                "question": "What is the statistical probability of a human couple having a girl child in any given pregnancy?",
                "options": [
                    "25%",
                    "50%",
                    "75%",
                    "100%"
                ],
                "answer": 1,
                "hint": "Consider the equal ratio of X-bearing and Y-bearing sperm produced by the father.",
                "explanation": "Father produces X and Y sperm in equal numbers (50% each), giving an exact 50% (1 in 2) probability of conceiving a female child."
            }
        ]
    }
]

if __name__ == "__main__":
    print("=== CHECKING SLIDES 9 TO 16 DATA ===")
    for s in SLIDES_PART2:
        title_words = len(s["title"].split())
        speech_words = len(s["speech"].split())
        print(f"Slide {s['id']}: '{s['title']}' | Title words: {title_words} | Speech words: {speech_words}")
        assert title_words <= 3, f"Title has >3 words: {s['title']}"
        assert 195 <= speech_words <= 215, f"Speech words out of range: {speech_words} in Slide {s['id']}"

    with open(".agents/c10s_ch8_part2.json", "w", encoding="utf-8") as f:
        json.dump(SLIDES_PART2, f, indent=2)
    print("Saved .agents/c10s_ch8_part2.json successfully!")
