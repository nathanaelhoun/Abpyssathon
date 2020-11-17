-- DELETE ALL
DROP TABLE score; 

-- CREATE ALL

CREATE TABLE score (
    sco_guild_id BIGINT,
    sco_member_id BIGINT,
    sco_value INT DEFAULT 0 NOT NULL,
    PRIMARY KEY (sco_guild_id, sco_member_id)
);