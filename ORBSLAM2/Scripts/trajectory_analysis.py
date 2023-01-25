import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

import bagpy
from bagpy import bagreader


def plot_test():
    camera = pd.read_csv(
        '../Trajectories/fr1_desk/CameraTrajectory.txt', sep=" ", header=None)
    keyframe = pd.read_csv(
        '../Trajectories/fr1_desk/KeyFrameTrajectory.txt', sep=" ", header=None)
    ground_truth = pd.read_csv(
        '../Trajectories/fr1_desk/groundtruth.txt', sep=" ", header=2)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = keyframe[1]
    y = keyframe[2]
    z = keyframe[3]
    x_true = ground_truth['tx'] - ground_truth['tx'][0]
    y_true = ground_truth['ty'] - ground_truth['ty'][0]
    z_true = ground_truth['tz'] - ground_truth['tz'][0]


    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.scatter(x, y, z)
    ax.scatter(x_true[0], y_true[0], z_true[0], color='r', s=400)
    ax.scatter(x[0], y[0], z[0], color='k', s=400)

    ax.scatter(x_true, y_true, z_true)
    #ax.set_box_aspect([1,1,1])

    plt.show()
    plt.close()

    print(rmse(x_true, x))
    print(rmse(y_true, y))
    print(rmse(z_true, z))
    print("")


def rmse(truth, actual):
    return np.sqrt(((truth-actual)**2).mean())


def process_gps(data):
    eastings = data[0] - data[0].mean()
    northings = data[1] - data[1].mean()
    alt = data[2] - data[1].mean()

    eastings -= eastings[0]
    northings -= northings[0]
    alt -= alt[0]

    return [eastings, northings, alt]


def plot_test1_ruggles():
    gps = pd.read_csv('../GPS data/test1-ruggles.txt', sep=" ", header=None)
    keyframes = pd.read_csv('../Trajectories/ruggles/better/KeyFrameTrajectory.txt', sep=" ", header=None)
    camera = pd.read_csv('../Trajectories/ruggles/better/CameraTrajectory.txt', sep=" ", header=None)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    eastings = gps[0] - gps[0].mean()
    northings = gps[1] - gps[1].mean()
    alt = gps[2] - gps[2].mean()

    eastings -= eastings[0]
    northings -= northings[0]
    alt -= alt[0]

    X = camera[1]
    Y = camera[2]
    Z = camera[3]

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_zlabel("Z [m]")

    ax.scatter(-4*Z, 3.5*X, Y, label="ORB-SLAM Camera Points")
    ax.scatter(eastings, northings, alt, label='GPS')
    # ax.scatter(eastings[0], northings[0], alt[0], color='r', s=400)
    # ax.scatter(X[0], Y[0], Z[0], color='k', s=400)

    plt.title("Test 1: Ruggles roundabout")
    plt.legend()
    plt.show()

    plt.close()


def plot_test2_nu_fenway():
    gps = pd.read_csv('../GPS data/test2-nu.txt', sep=" ", header=None)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    eastings = gps[0]
    northings = gps[1]
    alt = gps[2]

    east_offset = eastings.mean()
    north_offset = northings.mean()
    alt_offset = alt.min()

    eastings -= east_offset
    northings -= north_offset
    alt -= alt_offset

    ax.set_xlabel("Easting [m]")
    ax.set_ylabel("Northing [m]")
    ax.set_zlabel("Altitude [m]")

    ax.scatter(eastings, northings, alt)
    # ax.scatter(x_true, y_true, z_true)
    ax.set_box_aspect([1,1,1])

    plt.title("Test 2: Around NEU")
    plt.show()

    plt.close()


def plot_test3_long_run():
    gps = pd.read_csv('../GPS data/test3-long_run.txt', sep=" ", header=None)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    eastings = gps[0]
    northings = gps[1]
    alt = gps[2]

    east_offset = eastings.mean()
    north_offset = northings.mean()
    alt_offset = alt.min()

    eastings -= east_offset
    northings -= north_offset
    alt -= alt_offset

    ax.set_xlabel("Easting [m]")
    ax.set_ylabel("Northing [m]")
    ax.set_zlabel("Altitude [m]")

    ax.scatter(eastings, northings, alt)
    # ax.scatter(x_true, y_true, z_true)
    ax.set_box_aspect([1,1,1])

    plt.title("Test 3: Long run around NU")
    plt.show()

    plt.close()


def plot_occluded():
    keyframes = pd.read_csv('../Trajectories/occluded/KeyFrameTrajectory.txt', sep=" ", header=None)
    camera = pd.read_csv('../Trajectories/occluded/CameraTrajectory.txt', sep=" ", header=None)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = camera[1]
    Y = camera[2]
    Z = camera[3]

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_zlabel("Z [m]")

    ax.scatter(X, Y, Z, label="ORB-SLAM KeyFrames")

    plt.title("Library: Occluded")
    # plt.legend()
    plt.show()

    plt.close()


def plot_occluded_better():
    keyframes = pd.read_csv('../Trajectories/occluded/better/KeyFrameTrajectory.txt', sep=" ", header=None)
    camera = pd.read_csv('../Trajectories/occluded/better/CameraTrajectory.txt', sep=" ", header=None)

    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    ax = fig.add_subplot(111)

    X = camera[1]
    Y = camera[2]
    # Z = keyframes[3]

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    # ax.set_zlabel("Z [m]")

    ax.scatter(X, Y, label="ORB-SLAM KeyFrames")

    plt.title("Test 3: Occlusions")
    # plt.legend()
    plt.show()

    plt.close()


def plot_highway():
    keyframes = pd.read_csv('../Trajectories/highway/KeyFrameTrajectory.txt', sep=" ", header=None)
    camera = pd.read_csv('../Trajectories/highway/CameraTrajectory.txt', sep=" ", header=None)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = camera[1]
    Y = camera[2]
    Z = camera[3]

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_zlabel("Z [m]")

    ax.scatter(X, Y, Z, label="ORB-SLAM KeyFrames")

    plt.title("Library: Highway")
    plt.show()

    plt.close()


def plot_highway_better():
    keyframes = pd.read_csv('../Trajectories/highway/better/KeyFrameTrajectory.txt', sep=" ", header=None)
    camera = pd.read_csv('../Trajectories/highway/better/CameraTrajectory.txt', sep=" ", header=None)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = keyframes[1]
    Y = keyframes[2]
    Z = keyframes[3]

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_zlabel("Z [m]")

    ax.scatter(X, Y, Z, label="ORB-SLAM KeyFrames")

    plt.title("Test 5: Dynamic Environment (highway video)")
    plt.show()

    plt.close()


def plot_ceiling():
    keyframes = pd.read_csv('../Trajectories/ceiling-better/KeyFrameTrajectory.txt', sep=" ", header=None)
    camera = pd.read_csv('../Trajectories/ceiling-better/CameraTrajectory.txt', sep=" ", header=None)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = keyframes[1]
    Y = keyframes[2]
    Z = keyframes[3]

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_zlabel("Z [m]")

    ax.scatter(X, Y, Z, label="ORB-SLAM KeyFrames")

    plt.title("Test 6: Featureless Environment (ceiling)")
    plt.show()

    plt.close()
    print(len(camera[1]), len(keyframes[1]))
    print(camera[0][0], keyframes[0][0])
    print(camera[0][63], keyframes[0][41])
    print(camera[0][63] - camera[0][0], keyframes[0][41] - keyframes[0][0])


def plot_rotations():
    keyframes = pd.read_csv('../Trajectories/rotations/KeyFrameTrajectory.txt', sep=" ", header=None)
    camera = pd.read_csv('../Trajectories/rotations/CameraTrajectory.txt', sep=" ", header=None)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = camera[1]
    Y = camera[2]
    Z = camera[3]

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_zlabel("Z [m]")

    ax.scatter(X, Y, Z, label="ORB-SLAM KeyFrames")

    plt.title("Library: Rotations")
    plt.show()

    plt.close()


def plot_rotations_better():
    keyframes = pd.read_csv('../Trajectories/rotations/better/KeyFrameTrajectory.txt', sep=" ", header=None)
    camera = pd.read_csv('../Trajectories/rotations/better/CameraTrajectory.txt', sep=" ", header=None)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = camera[1]
    Y = camera[2]
    Z = camera[3]

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_zlabel("Z [m]")

    ax.scatter(X, Y, Z, label="ORB-SLAM Camera Points")

    plt.title("Test 4: Rotations")
    plt.show()

    plt.close()


def plot_fenway1():
    keyframes = pd.read_csv('../Trajectories/nu-fenway1/KeyFrameTrajectory.txt', sep=" ", header=None)
    camera = pd.read_csv('../Trajectories/nu-fenway1/CameraTrajectory.txt', sep=" ", header=None)
    gps = pd.read_csv('../GPS data/test2-nu.txt', sep=" ", header=None)

    gps_data = process_gps(gps)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = camera[1]
    Y = camera[2]
    Z = camera[3]

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_zlabel("Z [m]")

    ax.scatter(Z, -X, -Y, label="ORB-SLAM KeyFrames")
    ax.scatter(gps_data[0], gps_data[1], np.zeros(len(gps_data[2])), label='GPS')
    ax.scatter(gps_data[0][0], gps_data[1][0], gps_data[2][0], color='r', s=400)
    ax.scatter(X[0], Y[0], Z[0], color='k', s=400)

    plt.title("Car: NU-Fenway")
    plt.legend()
    plt.show()

    plt.close()


def plot_fenway1_better():
    keyframes = pd.read_csv('../Trajectories/nu-fenway2/KeyFrameTrajectory.txt', sep=" ", header=None)
    camera = pd.read_csv('../Trajectories/nu-fenway2/CameraTrajectory.txt', sep=" ", header=None)
    gps = pd.read_csv('../GPS data/test2-nu.txt', sep=" ", header=None)

    gps_data = process_gps(gps)
    im = plt.imread('../map.png')
    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    ax = fig.add_subplot(111)
    # implot = plt.imshow(im)

    X = camera[1]
    Y = camera[2]
    Z = camera[3]

    print(len(keyframes[1]), len(camera[1]))
    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    # ax.set_zlabel("Z [m]")

    # ax.scatter(gps_data[0], gps_data[1], np.zeros(len(gps_data[2])), label='GPS')
    ax.scatter(-1.8*gps_data[0]+840, -1.3*gps_data[1]+810, label='GPS')
    # ax.scatter(Z, X, Y, label="ORB-SLAM KeyFrames")
    # ax.scatter(5*X, 4*Z+10*Y, label="XZ")
    # ax.scatter(X,Y, label="XY")
    # ax.scatter(Z, X, label="ZX")
    # ax.scatter(Z, Y, label="ZY")
    # ax.scatter(Y, X, label="YX")
    ax.scatter(1.8*(5*Y+7*X)+840, -1.3*(5.4*Z)+810, label="Camera Points")
    plt.imshow(im)
    # ax.scatter(gps_data[0][0], gps_data[1][0], gps_data[2][0], color='r', s=400)
    # ax.scatter(X[0], Y[0], Z[0], color='k', s=400)

    plt.title("Test 2: NU-Fenway")
    # ax.set_box_aspect([1,1,1])

    plt.legend()
    plt.show()

    plt.close()


def plot_long_run():
    keyframes = pd.read_csv('../Trajectories/long run loops/KeyFrameTrajectory.txt', sep=" ", header=None)
    camera = pd.read_csv('../Trajectories/long run loops/CameraTrajectory.txt', sep=" ", header=None)
    gps = pd.read_csv('../GPS data/test3-long_run.txt', sep=" ", header=None)

    gps_data = process_gps(gps)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = camera[1]
    Y = camera[2]
    Z = camera[3]

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    ax.set_zlabel("Z [m]")

    ax.scatter(Z, X, Y, label="ORB-SLAM KeyFrames")
    # ax.scatter(gps_data[0], gps_data[1], np.zeros(len(gps_data[2])), label='GPS')
    # ax.scatter(gps_data[0][0], gps_data[1][0], gps_data[2][0], color='r', s=400)
    ax.scatter(X[0], Y[0], Z[0], color='k', s=400)

    plt.title("Car: NU-Fenway")
    plt.legend()
    plt.show()

    plt.close()


def plot_handheld():
    keyframes = pd.read_csv('../Trajectories/snell_walking_data_1 (2 loops)/KeyFrameTrajectory.txt', sep=" ", header=None)
    camera = pd.read_csv('../Trajectories/snell_walking_data_1 (2 loops)/CameraTrajectory.txt', sep=" ", header=None)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    X = camera[1]
    Y = camera[2]
    # Z = camera[3]

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    # ax.set_zlabel("Z [m]")

    ax.scatter(X, Y, label="ORB-SLAM Camera Points")

    plt.title("Test 8: Library Second Floor")
    plt.show()

    plt.close()


def plot_stable():
    keyframes = pd.read_csv('../Trajectories/snell_stab_data (1 loop)/KeyFrameTrajectory.txt', sep=" ",
                            header=None)
    camera = pd.read_csv('../Trajectories/snell_stab_data (1 loop)/CameraTrajectory.txt', sep=" ", header=None)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax = fig.add_subplot(111)


    X = camera[1]
    Y = camera[2]
    Z = camera[3]

    ax.set_xlabel("X [m]")
    ax.set_ylabel("Y [m]")
    # ax.set_zlabel("Z [m]")

    ax.scatter(Z, X, label="ORB-SLAM Camera Points")

    plt.title("Test 9: Library Second Floor (stable platform)")
    plt.show()

    plt.close()

# plot_test1_ruggles()
# plot_test()
# plot_test3_long_run()

# plot_occluded()
# plot_occluded_better()
# plot_highway()
# plot_highway_better()
# plot_ceiling()
# plot_rotations_better()
# plot_fenway1()
# plot_fenway1_better()
# plot_long_run()

# plot_handheld()
plot_stable()