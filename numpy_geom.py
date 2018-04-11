import numpy as np


def normalize(v):
    nv = np.linalg.norm(v)
    if nv > 0.0:
        v[0] = v[0]/nv
        v[1] = v[1]/nv
        v[2] = v[2]/nv
    return v


def skew_symmetric(v):
    """Returns a skew symmetric matrix from vector. p q r"""
    return np.array([[0, -v[2], v[1]],
                     [v[2], 0, -v[0]],
                     [-v[1], v[0], 0]])


def rotation_rpy(roll, pitch, yaw):
    """Returns a rotation matrix from roll pitch yaw. ZYX convention."""
    cr = np.cos(roll)
    sr = np.sin(roll)
    cp = np.cos(pitch)
    sp = np.sin(pitch)
    cy = np.cos(yaw)
    sy = np.sin(yaw)
    return np.array([[cy*cp,  cy*sp*sr - sy*cr,  cy*sp*cr + sy*sr],
                     [sy*cp,  sy*sp*sr + cy*cr,  sy*sp*cr - cy*sr],
                     [  -sp,             cp*sr,             cp*cr]])


def quaternion_rpy(roll, pitch, yaw):
    """Returns a quaternion ([x,y,z,w], w scalar) from roll pitch yaw ZYX
    convention."""
    cr = np.cos(roll/2.0)
    sr = np.sin(roll/2.0)
    cp = np.cos(pitch/2.0)
    sp = np.sin(pitch/2.0)
    cy = np.cos(yaw/2.0)
    sy = np.sin(yaw/2.0)
    x = sr*cp*cy - cr*sp*sy
    y = cr*sp*cy + sr*cp*sy
    z = cr*cp*sy - sr*sp*cy
    w = cr*cp*cy + sr*sp*sy
    nq = np.sqrt(x*x + y*y + z*z + w*w) 
    return np.array([x/nq,
                     y/nq,
                     z/nq,
                     w/nq])


def T_rpy(displacement, roll, pitch, yaw):
    """Homogeneous transformation matrix with roll pitch yaw."""
    T = np.zeros([4, 4])
    T[:3, :3] = rotation_rpy(roll, pitch, yaw)
    T[:3, 3] = displacement
    T[3, 3] = 1.0
    return T