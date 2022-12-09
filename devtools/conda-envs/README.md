# How to create and update a conda environment

## To develop the library

### Create env

If the name of the conda environment is `OpenENM`:

```bash
python create_conda_env.py -n OpenCTN -p 3.9 development_env.yaml
```

Now you can activate the environment with:

```bash
conda activate OpenCTN
```

### Update env

With the environment activated:

```bash
update_conda_env.py development_env.yaml
```

or

```bash
mamba env update --file development_env.yaml
```
