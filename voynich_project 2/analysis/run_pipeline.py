
import yaml, os
from scripts import ingest, segment, baselines, morphology_bpe, cipher_diagnostics

def main():
    with open('voynich_project/analysis/config.yaml') as f:
        config = yaml.safe_load(f)

    print("[1] Ingesting data...")
    ingest.run(config)
    print("[2] Segmenting...")
    segment.run(config)
    print("[3] Running baselines...")
    baselines.run(config)
    print("[4] Morphology...")
    morphology_bpe.run(config)
    print("[5] Cipher diagnostics...")
    cipher_diagnostics.run(config)
    print("Pipeline complete. Outputs in output/.")

if __name__ == "__main__":
    main()
