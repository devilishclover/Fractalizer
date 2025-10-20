from pathlib import Path

def parse(fractalFile):
    """
    Parses a fractal data file into a dictionary
    returns a tuple of the form (NAME, DICT)
    """
    data = {
        'fname': fractalFile,
        'name': Path(fractalFile).stem
    }
    
    with open(fractalFile) as f:
        for line in f:
            if line == '\n' or line.lstrip().startswith('#'):
                continue
            line_data = line.replace(' ', '').rstrip().split(":")
            if len(line_data) == 2:
                data[line_data[0].lower()] = line_data[1].lower()
            else:
            # too many colons
                raise RuntimeError(f"error: too many colons")
            
    # Cast items to the correct type
    if 'centerx' in data:
        data['centerx'] = float(data['centerx'])
    if 'centery' in data:
        data['centery'] = float(data['centery'])
    if 'axislength' in data:
        data['axislength'] = float(data['axislength'])
    if 'preal' in data:
        data['preal'] = float(data['preal'])
    if 'pimag' in data:
        data['pimag'] = float(data['pimag'])
    if 'creal' in data:
        data['creal'] = float(data['creal'])
    if 'cimag' in data:
        data['cimag'] = float(data['cimag'])
    if 'iterations' in data:
        data['iterations'] = int(data['iterations'])
    if 'pixels' in data:
        data['pixels'] = int(data['pixels'])
    
    # missing a key check
    required_keys = ['centerx', 'centery', 'axislength', 'name']
    missing_keys = []
    for key in required_keys:
        if key not in data:
            missing_keys.append(key)
    if missing_keys:
        raise RuntimeError(f"Missing required keys: {', '.join(missing_keys)}")
    
    # axisLength check
    if 'axislength' in data and data['axislength'] <= 0:
        raise ValueError("axislength must be positive")

    tupple = (data['name'], data)
    return tupple
         