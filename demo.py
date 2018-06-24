import gazu

gazu.set_host("http://localhost/api")
gazu.log_in("admin@example.com", "default")

bbb = gazu.project.new_project("Big Buck Bunny")
agent327 = gazu.project.new_project("Agent 327")
caminandes = gazu.project.new_project("Caminandes Llamigos")

characters = gazu.asset.new_asset_type("Characters")
props = gazu.asset.new_asset_type("Props")
environment = gazu.asset.new_asset_type("Props")
fx = gazu.asset.new_asset_type("FX")


asset_desc = [
    (characters, "Lama"),
    (characters, "Baby Pingoo"),
    (characters, "Pingoo"),
    (environment, "Mine"),
    (environment, "Pool"),
    (environment, "Railroad"),
    (fx, "smoke"),
    (fx, "wind"),
    (props, "berry"),
    (props, "flower")
]

assets = []
shots = []

for (asset_type, asset_name) in asset_desc:
    assets.append(
        gazu.asset.new_asset(caminandes, asset_type, asset_name)
    )


for episode_name in ["E01", "E02", "E03"]:
    episode = gazu.shot.new_episode(caminandes, episode_name)

    for sequence_name in ["SE01", "SE02", "SE03"]:
        sequence = gazu.shot.new_sequence(
            caminandes, episode, sequence_name)

        for shot_name in ["SH01", "SH02", "SH03"]:
            shots.append(
                gazu.shot.new_shot(caminandes, sequence, shot_name)
            )


modeling = gazu.task.get_task_type_by_name("Modeling")
setup = gazu.task.get_task_type_by_name("Setup")
animation = gazu.task.get_task_type_by_name("Animation")
render = gazu.task.get_task_type_by_name("Render")
compositing = gazu.task.get_task_type_by_name("Compositing")

for asset in assets:
    gazu.task.new_task(asset, modeling)
    gazu.task.new_task(asset, setup)

for shot in shots:
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
    "/pictures/thumbnais/projects/%s" % caminandes["id"],
    "fixtures/v1.png"
)

persons = [
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

file_paths = [
    "fixtures/th_shots/caminandes_llamigos_e01_se01_s01.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se01_s02.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se01_s03.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se01_s04.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se01_s05.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se01_s06.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se01_s07.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se01_s08.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se01_s09.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s01.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s02.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s03.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s04.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s05.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s06.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s07.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s08.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s09.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s01.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s02.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s03.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s04.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s05.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s06.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s07.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s08.png",
    "fixtures/th_shots/caminandes_llamigos_e01_se02_s09.png"
]

done = gazu.task.get_task_status_by_name("Done")
wfa = gazu.task.get_task_status_by_name("Waiting For Approval")

for (index, shot) in enumerate(shots):
    task_anim = gazu.task.get_task_by_name(shot, animation)
    comment = gazu.task.add_comment(task_anim, wfa, "New preview")
    preview_file = gazu.task.add_preview(task_anim, comment, file_paths[index])
    gazu.task.set_main_preview(shot, preview_file)
    comment = gazu.task.add_comment(task_anim, done, "Done")
