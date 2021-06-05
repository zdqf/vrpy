from networkx import from_numpy_matrix, set_node_attributes, relabel_nodes, DiGraph
from numpy import array
from vrpy import VehicleRoutingProblem


class TestIssue79:
    def setup(self):

        distance_ = [
            [
                0,
                0.0,
                0.0,
                34.751182089808005,
                92.30245516008434,
                40.1681913442985,
                139.77829026093886,
                22.427641389383695,
                184.16196166082054,
                24.56323283561296,
                120.32361659641211,
                32.4378310152284,
                67.38909304866816,
                0.0,
            ],
            [
                0,
                0.0,
                0.0,
                34.751182089808005,
                92.30245516008434,
                40.1681913442985,
                139.77829026093886,
                22.427641389383695,
                184.16196166082054,
                24.56323283561296,
                120.32361659641211,
                32.4378310152284,
                67.38909304866816,
                0.0,
            ],
            [
                0,
                34.751182089808005,
                34.751182089808005,
                0.0,
                98.7079853042215,
                5.44379884433748,
                132.19619367955679,
                12.670008991256175,
                180.4339020413057,
                59.02280970986385,
                111.80230048333873,
                17.019169601216593,
                52.06928899775174,
                34.751182089808005,
            ],
            [
                0,
                92.30245516008434,
                92.30245516008434,
                98.7079853042215,
                0.0,
                100.22229866723093,
                61.488042505729055,
                92.72080465523338,
                95.63269969727976,
                90.58095214437495,
                49.80739772877824,
                111.78483468218113,
                60.09941865363839,
                92.30245516008434,
            ],
            [
                0,
                40.1681913442985,
                40.1681913442985,
                5.44379884433748,
                100.22229866723093,
                0.0,
                131.22379419294873,
                17.9495157302615,
                179.86968501771943,
                64.376780302526,
                110.81671081048268,
                20.17178955112936,
                50.836998290147,
                40.1681913442985,
            ],
            [
                0,
                139.77829026093886,
                139.77829026093886,
                132.19619367955679,
                61.488042505729055,
                131.22379419294873,
                0.0,
                131.60938240610648,
                49.833874922036394,
                145.2998753018322,
                20.40765785593238,
                148.57304976786813,
                80.3991613224116,
                139.77829026093886,
            ],
            [
                0,
                22.427641389383695,
                22.427641389383695,
                12.670008991256175,
                92.72080465523338,
                17.9495157302615,
                131.60938240610648,
                0.0,
                178.66012933702726,
                46.44000947768777,
                111.40463276346814,
                19.110204473855905,
                53.409038447894005,
                22.427641389383695,
            ],
            [
                0,
                184.16196166082054,
                184.16196166082054,
                180.4339020413057,
                95.63269969727976,
                179.86968501771943,
                49.833874922036394,
                178.66012933702726,
                0.0,
                185.80417023197256,
                69.739408771209,
                196.3770010004616,
                129.30466285486838,
                184.16196166082054,
            ],
            [
                0,
                24.56323283561296,
                24.56323283561296,
                59.02280970986385,
                90.58095214437495,
                64.376780302526,
                145.2998753018322,
                46.44000947768777,
                185.80417023197256,
                0.0,
                127.25510989846872,
                56.34697111358194,
                82.12357585699394,
                24.56323283561296,
            ],
            [
                0,
                120.32361659641211,
                120.32361659641211,
                111.80230048333873,
                49.80739772877824,
                110.81671081048268,
                20.40765785593238,
                111.40463276346814,
                69.739408771209,
                127.25510989846872,
                0.0,
                128.21818865240243,
                59.99584151749755,
                120.32361659641211,
            ],
            [
                0,
                32.4378310152284,
                32.4378310152284,
                17.019169601216593,
                111.78483468218113,
                20.17178955112936,
                148.57304976786813,
                19.110204473855905,
                196.3770010004616,
                56.34697111358194,
                128.21818865240243,
                0.0,
                68.79822623983333,
                32.4378310152284,
            ],
            [
                0,
                67.38909304866816,
                67.38909304866816,
                52.06928899775174,
                60.09941865363839,
                50.836998290147,
                80.3991613224116,
                53.409038447894005,
                129.30466285486838,
                82.12357585699394,
                59.99584151749755,
                68.79822623983333,
                0.0,
                67.38909304866816,
            ],
            [
                0,
                0.0,
                0.0,
                34.751182089808005,
                92.30245516008434,
                40.1681913442985,
                139.77829026093886,
                22.427641389383695,
                184.16196166082054,
                24.56323283561296,
                120.32361659641211,
                32.4378310152284,
                67.38909304866816,
                0.0,
            ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        demands = {
            0: 0,
            1: 24,
            2: 12,
            3: 22,
            4: 63,
            5: 44,
            6: 68,
            7: 41,
            8: 27,
            9: 38,
            10: 15,
            11: 17,
            12: 0,
        }

        # Transform distance matrix to DiGraph
        A_ = array(distance_, dtype=[("cost", int)])
        G_ = from_numpy_matrix(A_, create_using=DiGraph())

        # Set demand
        set_node_attributes(G_, values=demands, name="demand")

        # Relabel depot
        G_ = relabel_nodes(G_, {0: "Source", 13: "Sink"})

        # Define VRP
        self.prob = VehicleRoutingProblem(G_, load_capacity=100)

    def test_node_load(self):
        self.prob.solve()
        assert self.prob.best_value == 829
