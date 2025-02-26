from simple_pendulum.controllers.sac.sac_controller import SacController
from sim_parameters import torque_limit

name = "sac"
leaderboard_config = {"csv_path": "data/" + name + "/sim_swingup.csv",
                      "name": name,
                      "username": "dharnack"}

torque_limit = 2.0
model_path = "../data/models/sac_model.zip"

controller = SacController(model_path=model_path,
                           torque_limit=torque_limit,
                           use_symmetry=True,
                           state_representation=2)
