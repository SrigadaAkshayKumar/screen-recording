"""Hand patch after plan_builder: the recording has only ~2 s of cursor motion before the first
click (src 7.9-10.5), so the intro is played at 0.75x with a short lead hold instead of a 3 s hold."""
import json,sys
p='projects/script-05/work/plan.json'; d=json.load(open(p))
segs=d['segments']; k=next(i for i,s in enumerate(segs) if s['out_start']>=10.58-1e-6)
new=[dict(mode='hold',src_start=7.4,src_end=7.4,out_start=0.0,out_end=1.5),
     dict(mode='speed',src_start=7.4,src_end=11.0,out_start=1.5,out_end=6.32),
     dict(mode='speed',src_start=11.0,src_end=13.3,out_start=6.32,out_end=9.32),
     dict(mode='hold',src_start=13.3,src_end=13.3,out_start=9.32,out_end=10.58)]
d['segments']=new+segs[k:]
json.dump(d,open(p,'w'),indent=1)
