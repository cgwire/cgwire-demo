import os
import gazu

gazu.set_host("http://localhost/api")
gazu.log_in("admin@example.com", "default")

bbb = gazu.project.new_project("Big Buck Bunny")
agent327 = gazu.project.new_project("Agent 327")
caminandes = gazu.project.new_project("Caminandes", production_type="tvshow")

characters = gazu.asset.new_asset_type("Characters")
props = gazu.asset.new_asset_type("Props")
environment = gazu.asset.new_asset_type("Environment")
fx = gazu.asset.new_asset_type("FX")


asset_desc = [
    (characters, "Lama"),
    (characters, "Oti"),
    (characters, "Pingoo"),
    (environment, "Mine"),
    (environment, "Pool"),
    (environment, "Railroad"),
    (environment, "Oil Machine"),
    (fx, "Smoke"),
    (fx, "Wind"),
    (props, "Berry"),
    (props, "Flower"),
    (props, "Mine Cart"),
    (props, "Train")
]

assets = []
shots = []

for (asset_type, asset_name) in asset_desc:
    assets.append(
        gazu.asset.new_asset(caminandes, asset_type, asset_name)
    )

for episode_name in ["E01"]:
    episode = gazu.shot.new_episode(caminandes, episode_name)

    for sequence_name in ["SE01", "SE02", "SE03"]:
        sequence = gazu.shot.new_sequence(
            caminandes, episode, sequence_name)

        for shot_name in [
            "SH001",
            "SH002",
            "SH003",
            "SH004",
            "SH005",
            "SH006",
            "SH007",
            "SH008",
            "SH009",
            "SH010",
            "SH011"
        ]:
            shots.append(
                gazu.shot.new_shot(caminandes, sequence, shot_name)
            )
for episode_name in ["E02"]:
    episode = gazu.shot.new_episode(caminandes, episode_name)

    for sequence_name in ["SE01", "SE02"]:
        sequence = gazu.shot.new_sequence(
            caminandes, episode, sequence_name)

        for shot_name in ["SH001", "SH002", "SH003"]:
            shots.append(
                gazu.shot.new_shot(caminandes, sequence, shot_name)
            )

for episode_name in ["E03"]:
    episode = gazu.shot.new_episode(caminandes, episode_name)

    for sequence_name in ["SE01", "SE02", "SE03"]:
        sequence = gazu.shot.new_sequence(
            caminandes, episode, sequence_name)

        for shot_name in [
            "SH001",
            "SH002",
            "SH003",
            "SH004",
            "SH005",
            "SH006",
            "SH007"
        ]:
            shots.append(
                gazu.shot.new_shot(caminandes, sequence, shot_name)
            )

modeling = gazu.task.get_task_type_by_name("Modeling")
setup = gazu.task.get_task_type_by_name("Setup")
storyboard = gazu.task.get_task_type_by_name("Storyboard")
layout = gazu.task.get_task_type_by_name("Layout")
animation = gazu.task.get_task_type_by_name("Animation")
render = gazu.task.get_task_type_by_name("Render")
compositing = gazu.task.get_task_type_by_name("Compositing")

for asset in assets:
    gazu.task.new_task(asset, modeling)
    gazu.task.new_task(asset, setup)

for shot in shots:
    gazu.task.new_task(shot, storyboard)
    gazu.task.new_task(shot, animation)
    gazu.task.new_task(shot, render)
    gazu.task.new_task(shot, compositing)

lama = gazu.asset.get_asset_by_name(caminandes, "Lama")
pingoo = gazu.asset.get_asset_by_name(caminandes, "Pingoo")
berry = gazu.asset.get_asset_by_name(caminandes, "Berry")


casting = [
    {
        "asset_id": lama["id"],
        "nb_occurences": 1
    },
    {
        "asset_id": pingoo["id"],
        "nb_occurences": 1
    },
    {
        "asset_id": berry["id"],
        "nb_occurences": 2
    }
]
gazu.shot.update_casting(shots[0], casting)
gazu.shot.update_casting(shots[1], casting)
gazu.shot.update_casting(shots[2], casting)
gazu.shot.update_casting(shots[3], casting)

gazu.client.upload(
   "/pictures/thumbnails/projects/%s" % caminandes["id"],
   "fixtures/v1.png"
)

'''persons = [
    {
        "first_name": "Alicia",
        "last_name": "Cooper",
        "email": "alicia@cg-wire.com",
        "phone": "+33 6 82 38 19 08",
        "role": "user",
        "name": "alicia"
    },
    {
        "first_name": "Michael",
        "last_name": "Byrd",
        "email": "michael@cg-wire.com",
        "phone": "+33 6 32 45 12 45",
        "role": "user",
        "name": "michael"
    },
    {
        "first_name": "Ann",
        "last_name": "Kennedy",
        "email": "ann@cg-wire.com",
        "phone": "+33 6 32 45 12 45",
        "role": "user",
        "name": "ann"
    },
    {
        "first_name": "Brennan",
        "last_name": "Mason",
        "email": "brennan@cg-wire.com",
        "phone": "+33 6 43 42 13 21",
        "role": "user",
        "name": "brennan"
    },
    {
        "first_name": "David",
        "last_name": "Penna",
        "email": "david@cg-wire.com",
        "phone": "+33 6 08 98 92 12",
        "role": "user",
        "name": "david"
    },
    {
        "first_name": "Rachel",
        "last_name": "Shelton",
        "email": "rachel@cg-wire.com",
        "phone": "+33 6 92 38 91 23",
        "role": "user",
        "name": "rachel"
    },
    {
        "first_name": "Frank",
        "last_name": "Rousseau",
        "email": "frank@cg-wire.com",
        "phone": "+33 6 07 08 95 78",
        "role": "user",
        "name": "frank"
    }
]

for person in persons:
    personfull = gazu.person.new_person(
        person["first_name"],
        person["last_name"],
        person["email"],
        person["phone"],
        person["role"]
    )
    gazu.person.set_avatar(personfull, "fixtures/fake_user/%s.png" % person["name"])
'''

file_paths_modeling = [
    "fixtures/th_assets/lama.png",
    "fixtures/th_assets/ep01/oti.png",
    "fixtures/th_assets/ep01/pingoo.png",
    "fixtures/th_assets/ep01/mine.png",
    "fixtures/th_assets/ep01/pool.png",
    "fixtures/th_assets/ep01/railroad.jpg",
    "fixtures/th_assets/ep01/oil_machine.png",
    "fixtures/th_assets/ep01/smoke.png",
    "fixtures/th_assets/ep01/wind.png",
    "fixtures/th_assets/ep01/berry.png",
    "fixtures/th_assets/ep01/flower.png",
    "fixtures/th_assets/ep01/cart.png",
    "fixtures/th_assets/ep01/train.png",
  ]


file_paths_sb = [
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE01_SH01.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE01_SH02.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE01_SH03.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE01_SH04.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE01_SH05.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE01_SH06.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE01_SH07.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE01_SH08.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE01_SH09.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE01_SH10.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE01_SH11.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE02_SH01.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE02_SH02.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE02_SH03.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE02_SH04.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE02_SH05.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE02_SH06.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE02_SH07.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE02_SH08.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE02_SH09.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE02_SH10.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE02_SH11.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE03_SH01.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE03_SH02.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE03_SH03.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE03_SH04.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE03_SH05.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE03_SH06.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE03_SH07.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE03_SH08.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE03_SH09.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE03_SH10.png",
    "fixtures/th_shots/ep01/SB/caminandes_llamigos_E01_SE03_SH11.png",
]

file_paths_animation = [
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE01_SH01.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE01_SH02.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE01_SH03.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE01_SH04.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE01_SH05.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE01_SH06.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE01_SH07.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE01_SH08.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE01_SH09.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE01_SH10.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE01_SH11.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE02_SH01.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE02_SH02.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE02_SH03.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE02_SH04.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE02_SH05.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE02_SH06.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE02_SH07.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE02_SH08.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE02_SH09.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE02_SH10.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE02_SH11.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE03_SH01.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE03_SH02.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE03_SH03.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE03_SH04.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE03_SH05.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE03_SH06.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE03_SH07.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE03_SH08.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE03_SH09.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE03_SH10.png",
    "fixtures/th_shots/ep01/Anim/caminandes_llamigos_E01_SE03_SH11.png",
]


file_paths_render = [
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE01_SH01.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE01_SH02.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE01_SH03.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE01_SH04.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE01_SH05.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE01_SH06.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE01_SH07.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE01_SH08.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE01_SH09.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE01_SH10.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE01_SH11.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE02_SH01.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE02_SH02.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE02_SH03.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE02_SH04.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE02_SH05.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE02_SH06.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE02_SH07.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE02_SH08.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE02_SH09.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE02_SH10.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE02_SH11.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE03_SH01.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE03_SH02.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE03_SH03.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE03_SH04.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE03_SH05.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE03_SH06.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE03_SH07.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE03_SH08.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE03_SH09.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE03_SH10.png",
    "fixtures/th_shots/ep01/render/caminandes_llamigos_E01_SE03_SH11.png",
]

done = gazu.task.get_task_status_by_name("Done")
wfa = gazu.task.get_task_status_by_name("Waiting For Approval")
wip = gazu.task.get_task_status_by_name("Work In Progress")

for (index, asset) in enumerate(assets):
    task_modeling = gazu.task.get_task_by_name(asset, modeling)
    if index < len(file_paths_modeling) and \
       os.path.exists(file_paths_modeling[index]):
        comment = gazu.task.add_comment(task_modeling, wfa, "New preview")
        preview_file = gazu.task.add_preview(
            task_modeling,
            comment,
            file_paths_modeling[index]
        )
        gazu.task.set_main_preview(asset, preview_file)
        comment = gazu.task.add_comment(task_modeling, done, "Done")
        task_setup = gazu.task.get_task_by_name(asset, setup)
        comment = gazu.task.add_comment(task_setup, wip, "Getting started")

for (index, shot) in enumerate(shots):
    if index < len(file_paths_sb) and \
       os.path.exists(file_paths_sb[index]):
        task_sb = gazu.task.get_task_by_name(shot, storyboard)
        comment = gazu.task.add_comment(task_sb, wfa, "New preview")
        preview_file = gazu.task.add_preview(
            task_sb,
            comment,
            file_paths_sb[index]
        )
        gazu.task.set_main_preview(shot, preview_file)
        comment = gazu.task.add_comment(task_sb, done, "Done")

    if index < len(file_paths_animation) and \
       os.path.exists(file_paths_animation[index]):
        task_animation = gazu.task.get_task_by_name(shot, animation)
        comment = gazu.task.add_comment(task_animation, wfa, "New preview")
        preview_file = gazu.task.add_preview(
            task_animation,
            comment,
            file_paths_animation[index]
        )
        gazu.task.set_main_preview(shot, preview_file)
        comment = gazu.task.add_comment(task_animation, done, "Done")

    if index < len(file_paths_render) and \
       os.path.exists(file_paths_render[index]):
        task_render = gazu.task.get_task_by_name(shot, render)
        comment = gazu.task.add_comment(task_render, wfa, "New preview")
        preview_file = gazu.task.add_preview(
            task_render,
            comment,
            file_paths_render[index]
        )
        gazu.task.set_main_preview(shot, preview_file)
        comment = gazu.task.add_comment(task_render, done, "Done")
