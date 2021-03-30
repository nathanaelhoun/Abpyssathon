-- DELETE ALL
DROP TABLE score;
DROP TABLE roles;
DROP TABLE system; 

-- CREATE ALL
CREATE TABLE score (
    sco_guild_id BIGINT,
    sco_member_id BIGINT,
    sco_value INT DEFAULT 0 NOT NULL,
    PRIMARY KEY (sco_guild_id, sco_member_id)
);

CREATE TABLE roles (
    ro_guild_id BIGINT,
    ro_member_id BIGINT,
    ro_list VARCHAR(4096) DEFAULT 0 NOT NULL,
    PRIMARY KEY (ro_guild_id, ro_member_id)
);

CREATE TABLE system (
    key VARCHAR(16) NOT NULL,
    value VARCHAR(256) NOT NULL,
    PRIMARY KEY (key)
);
