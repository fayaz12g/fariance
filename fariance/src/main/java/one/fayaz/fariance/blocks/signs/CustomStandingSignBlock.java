package one.fayaz.fariance.blocks.signs;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.SoundType;
import net.minecraft.world.level.block.StandingSignBlock;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.properties.WoodType;
import net.minecraftforge.registries.RegistryObject;
import one.fayaz.fariance.ItemRegistry;

public class CustomStandingSignBlock extends StandingSignBlock {

    public CustomStandingSignBlock(Properties properties, WoodType woodType) {
        super(woodType, properties);
    }

    @Override
    public BlockEntity newBlockEntity(BlockPos pos, BlockState state) {
        return new CustomSignBlockEntity(pos, state);  // Use the custom block entity here
    }

    // Register this block in the ItemRegistry
    public static void register() {
        RegistryObject<Block> standingSign = ItemRegistry.BLOCKS.register("custom_standing_sign",
                () -> new CustomStandingSignBlock(BlockBehaviour.Properties.of()
                        .noCollission().strength(1.0F).sound(SoundType.WOOD), WoodType.OAK));
    }
}