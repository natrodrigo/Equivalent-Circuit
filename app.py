from flask import Flask, flash, redirect, render_template, request
import math

def decimal(value):
    if value > 999.999:
        value = value / 1000
        return f"{value:.2f}k"
    elif value < 1:
        value = value * 1000
        return f"{value:.2f}m"
    else:
        return f"{value:.2f}"

# Configure application
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        vca = float(request.form.get("vca"))
        ica = float(request.form.get("ica"))
        pca = float(request.form.get("pca"))
        vcc = float(request.form.get("vcc"))
        icc = float(request.form.get("icc"))
        pcc = float(request.form.get("pcc"))
        vp = float(request.form.get("vp"))
        vs = float(request.form.get("vs"))
        med_ca = request.form.get("medicao1")
        med_cc = request.form.get("medicao2")

        rc_p = (vca ** 2) / pca
        z_phi_p = vca / ica
        xm_p = 1 / math.sqrt(((1 / z_phi_p)**2) - ((1/rc_p)**2))
        a = vp/vs
        rc_s = rc_p / a**2
        z_phi_s = z_phi_p / a**2
        xm_s = xm_p / a**2
        pnucleo = vca**2 / rc_p
        zeq_p = vcc / icc
        req_p = pcc/ icc**2
        xeq_p = math.sqrt(zeq_p**2 - req_p**2)
        pcu = icc**2 * req_p
        zeq_s = zeq_p / a**2
        req_s = req_p / a**2
        xeq_s = xeq_p / a**2

        rp = req_p / 2
        xp  = xeq_p / 2
        rs = req_s / 2
        xs = xeq_s / 2

        rc_p= decimal(rc_p)
        z_phi_p= decimal(z_phi_p)
        xm_p=decimal(xm_p)
        a=decimal(a)
        rc_s = decimal(rc_s)
        z_phi_s = decimal(z_phi_s)
        xm_s=decimal(xm_s)
        pnucleo=decimal(pnucleo)
        zeq_p=decimal(zeq_p)
        req_p=decimal(req_p)
        xeq_p =decimal(xeq_p)
        pcu=decimal(pcu)
        zeq_s=decimal(zeq_s)
        req_s=decimal(req_s)
        xeq_s=decimal(xeq_s)
        rp=decimal(rp)
        xp=decimal(xp)
        rs=decimal(rs)
        xs=decimal(xs)


        return render_template("results.html", rc_p=rc_p, z_phi_p=z_phi_p, xm_p=xm_p, a=a,
        rc_s = rc_s, z_phi_s = z_phi_s, xm_s=xm_s, pnucleo=pnucleo, zeq_p=zeq_p,
        req_p=req_p, xeq_p =xeq_p, pcu=pcu, zeq_s=zeq_s, req_s=req_s, xeq_s=xeq_s,
        rp=rp, xp=xp, rs=rs, xs=xs, vp=vp, vs=vs)

    else:
        return render_template('index.html')


