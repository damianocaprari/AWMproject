export default {
    auth: {
        me: ($axios, userId) => $axios.$get(`users/${userId}/`),
        login: ($axios, data) => $axios.$post('auth/', {
            username: data.username,
            password: data.password
        }),
        register: ($axios, data) => $axios.$post('users/', {
            username: data.username,
            password: data.password,
            email: data.email,
            first_name: data.first_name,
            last_name: data.last_name
        })
    },
    updateUserProfile: ($axios, userId, data) => $axios.$put(`users/${userId}/`, {
        email: data.email,
        first_name: data.first_name,
        last_name: data.last_name
    }),

    updateMonster: ($axios, monsterId, data) => $axios.$put(`monsters/${monsterId}/`, {
        name: data.name,
        //image: data.image,
        size: data.size,

        type: data.type,
        subtype: data.subtype,
        alignment: data.alignment,
        armor_class: data.armor_class,
        armor_class_notes: data.armor_class_notes,

        hit_point: data.hit_point,
        hit_dice: data.hit_dice,
        ability_str: data.ability_str,
        ability_dex: data.ability_dex,
        ability_con: data.ability_con,
        ability_int: data.ability_int,
        ability_wis: data.ability_wis,
        ability_cha: data.ability_cha,
        challenge_rating: data.challenge_rating,

        traits: data.traits,
        speeds: data.speeds,
        saves: data.saves,
        skills: data.skills,
        damage_vulnerabilities: data.damage_vulnerabilities,
        damage_resistances: data.damage_resistances,
        condition_immunities: data.condition_immunities,
        damage_immunities: data.damage_immunities,
        senses: data.senses,
        languages: data.languages,
        special_abilities: data.special_abilities,
        actions: data.actions,
        legendary_actions: data.legendary_actions,
        //first_name: data.first_name,
        //last_name: data.last_name
    }),

    createMonster: ($axios, data) => $axios.$post(`monsters/`, data, {
        headers: {
            Accept: "text/html"
        }
    }),

    createSpell: ($axios, data) => $axios.$post(`spells/`, data, {
        headers: {
            Accept: "text/html"
        }
    })
    // o gli passi data così come' se tutti i nomi sono uguali, oppure mappi come sopra con le graffe intorno perche oggetto

}
