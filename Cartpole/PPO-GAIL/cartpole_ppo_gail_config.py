from easydict import EasyDict


cartpole_ppo_gail_config = dict(
    exp_name='cartpole_ppo_gail_seed0',
    env=dict(
        collector_env_num=8,
        evaluator_env_num=5,
        n_evaluator_episode=5,
        stop_value=195,
        replay_path='cartpole_ppo_gail_seed0/video',
    ),
    reward_model=dict(
        type='gail',
        input_size=5,
        hidden_size=128,
        batch_size=64,
        learning_rate=1e-3,
        update_per_collect=128,
        # Users should add their own model path here. Model path should lead to a model.
        # Absolute path is recommended.
        # In DI-engine, it is ``exp_name/ckpt/ckpt_best.pth.tar``.
        # If collect_data is True, we will use this expert_model_path to collect expert data first, rather than we
        # will load data directly from user-defined data_path
        expert_model_path='cartpole_ppo_offpolicy_seed0/ckpt/ckpt_best.pth.tar',
        collect_count=1000,
    ),
    policy=dict(
        cuda=False,
        model=dict(
            obs_shape=4,
            action_shape=2,
            encoder_hidden_size_list=[64, 64, 128],
            critic_head_hidden_size=128,
            actor_head_hidden_size=128,
            action_space='discrete',
        ),
        learn=dict(
            update_per_collect=6,
            batch_size=64,
            learning_rate=0.001,
            value_weight=0.5,
            entropy_weight=0.01,
            clip_ratio=0.2,
            learner=dict(hook=dict(save_ckpt_after_iter=1000)),
        ),
        collect=dict(
            n_sample=128,
            unroll_len=1,
            discount_factor=0.9,
            gae_lambda=0.95,
        ),
        eval=dict(evaluator=dict(eval_freq=10, )),
        other=dict(replay_buffer=dict(replay_buffer_size=5000))
    ),
)
cartpole_ppo_gail_config = EasyDict(cartpole_ppo_gail_config)
main_config = cartpole_ppo_gail_config
cartpole_ppo_gail_create_config = dict(
    env=dict(
        type='cartpole',
        import_names=['dizoo.classic_control.cartpole.envs.cartpole_env'],
    ),
    env_manager=dict(type='base'),
    policy=dict(type='ppo_offpolicy'),
)
cartpole_ppo_gail_create_config = EasyDict(cartpole_ppo_gail_create_config)
create_config = cartpole_ppo_gail_create_config

if __name__ == "__main__":
    from ding.entry import serial_pipeline_gail
    from dizoo.classic_control.cartpole.config import cartpole_ppo_offpolicy_config, cartpole_ppo_offpolicy_create_config
    expert_main_config = cartpole_ppo_offpolicy_config
    expert_create_config = cartpole_ppo_offpolicy_create_config
    serial_pipeline_gail(
        (main_config, create_config), (expert_main_config, expert_create_config),
        max_env_step=1000000,
        seed=0,
        collect_data=True
    )