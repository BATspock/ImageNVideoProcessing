
def curvature(f):
    fy, fx = grad(f)
    norm = np.sqrt(fx**2 + fy**2)
    Nx = fx / (norm + 1e-8)
    Ny = fy / (norm + 1e-8)
    return div(Nx, Ny)


def div(fx, fy):
    fyy, fyx = grad(fy)
    fxy, fxx = grad(fx)
    return fxx + fyy


def dot(x, y, axis=0):
    return np.sum(x * y, axis=axis)


v = 1.
dt = 1.

g = stopping_fun(img_smooth, alpha)
dg = grad(g)

for i in range(n_iter):
    dphi = grad(phi)
    dphi_norm = norm(dphi)
    kappa = curvature(phi)

    smoothing = g * kappa * dphi_norm
    balloon = g * dphi_norm * v
    attachment = dot(dphi, dg)

    dphi_t = smoothing + balloon + attachment

    phi = phi + dt * dphi_t