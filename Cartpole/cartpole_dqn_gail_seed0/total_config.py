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
        'replay_path': 'cartpole_dqn_gail_seed0/video'
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
            'update_per_collect': 3,
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
            'n_sample': 64,
            'unroll_len': 1
        },
        'eval': {
            'evaluator': {
                'eval_freq': 10,
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
                'type': 'advanced',
                'replay_buffer_size': 20000,
                'max_use': float("inf"),
                'max_staleness': float("inf"),
                'alpha': 0.6,
                'beta': 0.4,
                'anneal_step': 100000,
                'enable_track_used_data': False,
                'deepcopy': False,
                'thruput_controller': {
                    'push_sample_rate_limit': {
                        'max': float("inf"),
                        'min': 0
                    },
                    'window_seconds': 30,
                    'sample_min_limit_ratio': 1
                },
                'monitor': {
                    'sampled_data_attr': {
                        'average_range': 5,
                        'print_freq': 200
                    },
                    'periodic_thruput': {
                        'seconds': 60
                    }
                },
                'cfg_type': 'AdvancedReplayBufferDict'
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
        'type': 'dqn_command',
        'priority': False,
        'priority_IS_weight': False,
        'discount_factor': 0.97,
        'nstep': 1,
        'cfg_type': 'DQNCommandModePolicyDict'
    },
    'exp_name': 'cartpole_dqn_gail_seed0',
    'reward_model': {
        'type': 'gail',
        'input_size': 5,
        'hidden_size': 64,
        'batch_size': 64,
        'learning_rate': 0.001,
        'update_per_collect': 100,
        'expert_model_path': 'cartpole_dqn_seed0/ckpt/ckpt_best.pth.tar',
        'collect_count': 1000
    },
    'seed': 0
}
