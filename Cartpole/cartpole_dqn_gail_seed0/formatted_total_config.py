from easydict import EasyDict

main_config = dict(
    exp_name='cartpole_dqn_gail_seed0',
    env=dict(
        manager=dict(
            episode_num=float('inf'),
            max_retry=1,
            retry_type='reset',
            auto_reset=True,
            step_timeout=None,
            reset_timeout=None,
            retry_waiting_time=0.1,
            cfg_type='BaseEnvManagerDict',
            type='base',
        ),
        stop_value=195,
        n_evaluator_episode=5,
        collector_env_num=8,
        evaluator_env_num=5,
        replay_path='cartpole_dqn_gail_seed0/video',
    ),
    policy=dict(
        model=dict(
            encoder_hidden_size_list=[128, 128, 64],
            obs_shape=4,
            action_shape=2,
            dueling=True,
        ),
        learn=dict(
            learner=dict(
                train_iterations=1000000000,
                dataloader=dict(
                    num_workers=0,
                ),
                log_policy=True,
                hook=dict(
                    load_ckpt_before_run='',
                    log_show_after_iter=100,
                    save_ckpt_after_iter=10000,
                    save_ckpt_after_run=True,
                ),
                cfg_type='BaseLearnerDict',
            ),
            update_per_collect=3,
            batch_size=64,
            learning_rate=0.001,
            target_update_freq=100,
            target_theta=0.005,
            ignore_done=False,
        ),
        collect=dict(
            collector=dict(
                deepcopy_obs=False,
                transform_obs=False,
                collect_print_freq=100,
                cfg_type='SampleSerialCollectorDict',
                type='sample',
            ),
            n_sample=64,
            unroll_len=1,
        ),
        eval=dict(
            evaluator=dict(
                eval_freq=10,
                render={'render_freq': -1, 'mode': 'train_iter'},
                cfg_type='InteractionSerialEvaluatorDict',
                stop_value=195,
                n_episode=5,
            ),
        ),
        other=dict(
            replay_buffer=dict(
                type='advanced',
                replay_buffer_size=20000,
                max_use=float('inf'),
                max_staleness=float('inf'),
                alpha=0.6,
                beta=0.4,
                anneal_step=100000,
                enable_track_used_data=False,
                deepcopy=False,
                thruput_controller=dict(
                    push_sample_rate_limit=dict(
                        max=float('inf'),
                        min=0,
                    ),
                    window_seconds=30,
                    sample_min_limit_ratio=1,
                ),
                monitor=dict(
                    sampled_data_attr=dict(
                        average_range=5,
                        print_freq=200,
                    ),
                    periodic_thruput=dict(
                        seconds=60,
                    ),
                ),
                cfg_type='AdvancedReplayBufferDict',
            ),
        ),
        on_policy=False,
        cuda=False,
        multi_gpu=False,
        bp_update_sync=True,
        traj_len_inf=False,
        priority=False,
        priority_IS_weight=False,
        discount_factor=0.97,
        nstep=1,
        cfg_type='DQNCommandModePolicyDict',
    ),
)
main_config = EasyDict(main_config)
main_config = main_config
create_config = dict(
    env=dict(
        type='cartpole',
        import_names=['dizoo.classic_control.cartpole.envs.cartpole_env'],
    ),
    env_manager=dict(
        cfg_type='BaseEnvManagerDict',
        type='base',
    ),
    policy=dict(type='dqn'),
)
create_config = EasyDict(create_config)
create_config = create_config
