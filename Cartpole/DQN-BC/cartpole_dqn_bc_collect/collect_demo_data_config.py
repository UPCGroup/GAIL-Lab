exp_config = {
    'env': {
        'manager': {
            'episode_num': float("inf"),
            'max_retry': 1,
            'retry_type': 'reset',
            'auto_reset': True,
            'step_timeout': None,
            'reset_timeout': None,
            'retry_waiting_time': 0.1,
            'cfg_type': 'BaseEnvManagerDict',
            'type': 'base'
        },
        'stop_value': 195,
        'n_evaluator_episode': 5,
        'type': 'cartpole',
        'import_names': ['dizoo.classic_control.cartpole.envs.cartpole_env'],
        'collector_env_num': 8,
        'evaluator_env_num': 5,
        'replay_path': 'cartpole_dqn_seed0/video'
    },
    'policy': {
        'model': {
            'encoder_hidden_size_list': [128, 128, 64],
            'obs_shape': 4,
            'action_shape': 2,
            'dueling': True
        },
        'learn': {
            'learner': {
                'train_iterations': 1000000000,
                'dataloader': {
                    'num_workers': 0
                },
                'log_policy': True,
                'hook': {
                    'load_ckpt_before_run': '',
                    'log_show_after_iter': 100,
                    'save_ckpt_after_iter': 10000,
                    'save_ckpt_after_run': True
                },
                'cfg_type': 'BaseLearnerDict'
            },
            'update_per_collect': 5,
            'batch_size': 64,
            'learning_rate': 0.001,
            'target_update_freq': 100,
            'target_theta': 0.005,
            'ignore_done': False
        },
        'collect': {
            'collector': {
                'deepcopy_obs': False,
                'transform_obs': False,
                'collect_print_freq': 100,
                'cfg_type': 'SampleSerialCollectorDict',
                'type': 'sample'
            },
            'n_sample': 8,
            'unroll_len': 1
        },
        'eval': {
            'evaluator': {
                'eval_freq': 40,
                'render': {
                    'render_freq': -1,
                    'mode': 'train_iter'
                },
                'cfg_type': 'InteractionSerialEvaluatorDict',
                'stop_value': 195,
                'n_episode': 5
            }
        },
        'other': {
            'replay_buffer': {
                'replay_buffer_size': 20000,
                'max_use': float("inf"),
                'train_iter_per_log': 100,
                'priority': False,
                'priority_IS_weight': False,
                'priority_power_factor': 0.6,
                'IS_weight_power_factor': 0.4,
                'IS_weight_anneal_train_iter': 100000,
                'priority_max_limit': 1000,
                'cfg_type': 'DequeBufferWrapperDict',
                'type': 'deque',
                'import_names': ['ding.data.buffer.deque_buffer_wrapper']
            },
            'eps': {
                'type': 'exp',
                'start': 0.95,
                'end': 0.1,
                'decay': 10000
            },
            'commander': {
                'cfg_type': 'BaseSerialCommanderDict'
            }
        },
        'on_policy': False,
        'cuda': False,
        'multi_gpu': False,
        'bp_update_sync': True,
        'traj_len_inf': False,
        'type': 'dqn',
        'priority': False,
        'priority_IS_weight': False,
        'discount_factor': 0.97,
        'nstep': 1,
        'cfg_type': 'DQNPolicyDict',
        'load_path': 'cartpole_dqn_seed0/ckpt/ckpt_best.pth.tar'
    },
    'exp_name': 'cartpole_dqn_bc_collect',
    'seed': 0
}
