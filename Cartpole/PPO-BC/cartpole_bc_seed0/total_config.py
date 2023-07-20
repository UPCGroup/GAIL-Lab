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
        'evaluator_env_num': 5
    },
    'policy': {
        'model': {
            'obs_shape': 4,
            'action_shape': 2,
            'encoder_hidden_size_list': [100, 2, 100]
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
                    'save_ckpt_after_iter': 1000,
                    'save_ckpt_after_run': True
                },
                'cfg_type': 'BaseLearnerDict'
            },
            'update_per_collect': 1,
            'batch_size': 100,
            'learning_rate': 0.01,
            'lr_decay': False,
            'decay_epoch': 30,
            'decay_rate': 0.1,
            'warmup_lr': 0.0001,
            'warmup_epoch': 3,
            'optimizer': 'Adam',
            'momentum': 0.9,
            'weight_decay': 0.0001,
            'ce_label_smooth': False,
            'show_accuracy': False,
            'tanh_mask': False,
            'train_epoch': 20
        },
        'collect': {
            'collector': {
                'deepcopy_obs': False,
                'transform_obs': False,
                'collect_print_freq': 100,
                'cfg_type': 'SampleSerialCollectorDict',
                'type': 'sample'
            },
            'unroll_len': 1,
            'noise': False,
            'noise_sigma': 0.2,
            'noise_range': {
                'min': -0.5,
                'max': 0.5
            }
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
                'type': 'advanced',
                'replay_buffer_size': 10000,
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
            'commander': {
                'cfg_type': 'BaseSerialCommanderDict'
            }
        },
        'on_policy': False,
        'cuda': False,
        'multi_gpu': False,
        'bp_update_sync': True,
        'traj_len_inf': False,
        'type': 'bc',
        'continuous': False,
        'action_shape': 19,
        'cfg_type': 'BehaviourCloningPolicyDict'
    },
    'exp_name': 'cartpole_bc_seed0',
    'seed': 0
}
