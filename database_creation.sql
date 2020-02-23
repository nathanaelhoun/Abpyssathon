-- DELETE ALL
DROP TABLE score; 
DROP TABLE score_category;

-- CREATE ALL
CREATE TABLE score_category (
    cat_guild_id BIGINT,
    cat_id SERIAL,
    cat_label VARCHAR(50) NOT NULL,
    PRIMARY KEY (cat_guild_id, cat_id)
);

CREATE TABLE score (
    sco_guild_id BIGINT,
    sco_member_id BIGINT,
    sco_category_id BIGINT,
    sco_value INT DEFAULT 0 NOT NULL,
    PRIMARY KEY (sco_guild_id, sco_member_id, sco_category_id),
    FOREIGN KEY (sco_guild_id, sco_category_id) REFERENCES score_category(cat_guild_id, cat_id)
);