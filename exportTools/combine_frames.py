from pathlib import Path
import shutil

dirs = [
    'frames_blah_2',
    'frames_converge_fast',
    'frames_converge_slow',
    'frames_decay_into_noise',
    'frames_default',
    'frames_double_center_knob',
    'frames_fast_to_noise',
    'frames_stuff',
]
dirs = [Path(d) for d in dirs]

out_dir = Path('combined_frames')

i = 0
for d in dirs:
    for frame_path in d.glob("*.png"):
        shutil.copy(frame_path, out_dir/ ('%04d.png' % i))
        i += 1
