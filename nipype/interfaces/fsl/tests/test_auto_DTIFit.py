# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..dti import DTIFit


def test_DTIFit_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        base_name=dict(
            argstr='-o %s',
            position=1,
            usedefault=True,
        ),
        bvals=dict(
            argstr='-b %s',
            mandatory=True,
            position=4,
        ),
        bvecs=dict(
            argstr='-r %s',
            mandatory=True,
            position=3,
        ),
        cni=dict(argstr='--cni=%s', ),
        dwi=dict(
            argstr='-k %s',
            mandatory=True,
            position=0,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        gradnonlin=dict(argstr='--gradnonlin=%s', ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        little_bit=dict(argstr='--littlebit', ),
        mask=dict(
            argstr='-m %s',
            mandatory=True,
            position=2,
        ),
        max_x=dict(argstr='-X %d', ),
        max_y=dict(argstr='-Y %d', ),
        max_z=dict(argstr='-Z %d', ),
        min_x=dict(argstr='-x %d', ),
        min_y=dict(argstr='-y %d', ),
        min_z=dict(argstr='-z %d', ),
        output_type=dict(),
        save_tensor=dict(argstr='--save_tensor', ),
        sse=dict(argstr='--sse', ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
    )
    inputs = DTIFit.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DTIFit_outputs():
    output_map = dict(
        FA=dict(),
        L1=dict(),
        L2=dict(),
        L3=dict(),
        MD=dict(),
        MO=dict(),
        S0=dict(),
        V1=dict(),
        V2=dict(),
        V3=dict(),
        tensor=dict(),
    )
    outputs = DTIFit.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
